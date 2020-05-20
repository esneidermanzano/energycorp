import React, { Component } from "react";
import { Map, Marker, Popup, TileLayer, LayersControl, FeatureGroup, Circle, LayerGroup } from 'react-leaflet';
import L from 'leaflet';
import axios from "axios";
import haversine from 'haversine-distance';
import {
  Button, Modal, ModalHeader, ModalBody, Form,
  FormGroup, Input
} from "reactstrap";

class TransformersMap extends Component {
  constructor() {
    super();
    this.state = {
      position: [3.4516, -76.5320],
      movingMarker: [3.4616, -76.5000],
      transformer: [],
      substations: [],
      counters: [],
      block: true,
      blockSub: true,
      blockCo: true,
      modal: false,
      counterInfo: {
        estrato: 0,
        direccion: ""
      }
    };
  }

  action = e => {
    // console.log([e.latlng.lat, e.latlng.lng]);
    this.setState({ movingMarker: [e.latlng.lat, e.latlng.lng] });
  }

  openToggle = obj => {
    this.setState({
      modal: true
    });
  }

  closeToggle = () => {
    this.setState({
      modal: false
    });
  }

  handleCounterInfo = e => {
    var info = { ...this.state.counterInfo };
    info[e.target.name] = e.target.value;
    this.setState({ counterInfo: info });
  }

  handleSubmitCounterInfo = e => {
    e.preventDefault();
    var trans = this.NearTransformator();
    // console.log(trans)
    var obj = {
      latitudeCounter: this.state.movingMarker[0].toString(),
      lengthCounter: this.state.movingMarker[1].toString(),
      value: 300,
      stratum: this.state.counterInfo.estrato,
      addressCounter: this.state.counterInfo.direccion,
      transformatorCounter: trans,
      is_active: true
    };

    axios.post("https://energycorp.herokuapp.com/api/energytransfers/counter/create/", obj)
      .then(res => {
        this.closeToggle();
        this.setState({
          counterInfo: {
            estrato: 0,
            direccion: ""
          }
        })
        this.getAllMapData();
      })
      .catch(err => {
        console.log(err);
      })
  }

  NearSubstation = () => {

    var a = {
      latitude: this.state.movingMarker[0],
      longitude: this.state.movingMarker[1]
    };

    var biggerDist = 999999;
    var bigger = 0;

    for (let i = 0; i < this.state.substations.length; i++) {

      var b = {
        latitude: this.state.substations[i].latitudeSubstation,
        longitude: this.state.substations[i].lengthSubstation
      };
      var d = haversine(a, b);
      // console.log(d)

      if (d < biggerDist) {
        biggerDist = d;
        bigger = this.state.substations[i].codeSubstation;
      }
    }
    return bigger;
  }

  NearTransformator = () => {

    var a = {
      latitude: this.state.movingMarker[0],
      longitude: this.state.movingMarker[1]
    };

    var biggerDist = 999999;
    var bigger = 0;

    for (let i = 0; i < this.state.transformer.length; i++) {

      var b = {
        latitude: this.state.transformer[i].latitudeTransformator,
        longitude: this.state.transformer[i].lengthTransformator
      };
      var d = haversine(a, b);
      // console.log(d)

      if (d < biggerDist) {
        biggerDist = d;
        bigger = this.state.transformer[i].codeTransformator;
      }
    }
    return bigger;
  }

  newPoint = (type) => {
    var obj;
    if (type === "transformer") {

      var sub = this.NearSubstation();

      obj = {
        // codeTransformator: this.state.transformer.length + 1,
        latitudeTransformator: this.state.movingMarker[0].toString(),
        lengthTransformator: this.state.movingMarker[1].toString(),
        is_active: true,
        substationTransformator: sub
      };

      axios.post("https://energycorp.herokuapp.com/api/energytransfers/transformator/create/", obj)
        .then(res => {
          this.getAllMapData();
        })
        .catch(err => {
          console.log(err);
        })

    } else if (type === "substations") {
      obj = {
        // codeSubstation: this.state.substations.length + 1,
        latitudeSubstation: this.state.movingMarker[0].toString(),
        lengthSubstation: this.state.movingMarker[1].toString(),
        is_active: true
      };

      axios.post("https://energycorp.herokuapp.com/api/energytransfers/substation/create/", obj)
        .then(res => {
          this.getAllMapData();
        })
        .catch(err => {
          console.log(err);
        })
    } else {
      this.openToggle();
    }
  }

  removePoint = (key, type) => {

    if (type === "transformer") {

      axios.delete("https://energycorp.herokuapp.com/api/energytransfers/transformator/delete/" + key)
        .then(res => {
          this.getAllMapData();
        })
        .catch(err => {
          console.log(err);
        })

    } else if (type === "substations") {

      axios.delete("https://energycorp.herokuapp.com/api/energytransfers/substation/delete/" + key)
        .then(res => {
          this.getAllMapData();
        })
        .catch(err => {
          console.log(err);
        })
    } else {
      axios.delete("https://energycorp.herokuapp.com/api/energytransfers/counter/delete/" + key)
        .then(res => {
          this.getAllMapData();
        })
        .catch(err => {
          console.log(err);
        })
    }
  }

  inactiveActivePoint = (key, val, type) => {
    if (type === "transformer") {
      axios.patch("https://energycorp.herokuapp.com/api/energytransfers/transformator/inactivate/" + key + "/", { "is_active": !val })
        .then(res => {
          this.getAllMapData();
        })
        .catch(err => {
          console.log(err);
        })

    } else if (type === "substations") {
      axios.patch("https://energycorp.herokuapp.com/api/energytransfers/substation/inactivate/" + key + "/", { "is_active": !val })
        .then(res => {
          this.getAllMapData();
        })
        .catch(err => {
          console.log(err);
        })
    } else {
      axios.patch("https://energycorp.herokuapp.com/api/energytransfers/counter/inactivate/" + key + "/", { "is_active": !val })
        .then(res => {
          this.getAllMapData();
        })
        .catch(err => {
          console.log(err);
        })
    }
  }

  blockMarkers = e => {
    if (e.name === "Transformers") {
      this.setState({ block: !this.state.block });
    } else if (e.name === "Substations") {
      this.setState({ blockSub: !this.state.blockSub });
    } else {
      this.setState({ blockCo: !this.state.blockCo });
    }
  }

  async getAllMapData() {

    const res = await fetch('https://energycorp.herokuapp.com/api/energytransfers/transformator');
    const res2 = await fetch('https://energycorp.herokuapp.com/api/energytransfers/substation/');
    const res3 = await fetch('https://energycorp.herokuapp.com/api/energytransfers/counter/ ')

    const data = await res.json();
    const data2 = await res2.json();
    const data3 = await res3.json();

    console.log(data, data2, data3);

    var ts = [];
    var sb = [];
    var co = [];

    for (let i = 0; i < data.length; i++) {
      ts.push(data[i]);
    }

    for (let i = 0; i < data2.length; i++) {
      sb.push(data2[i]);
    }

    for (let i = 0; i < data3.length; i++) {
      co.push(data3[i]);
    }

    this.setState({ transformer: ts, substations: sb, counters: co });
  }

  componentDidMount() {
    this.getAllMapData();
  }

  render() {

    // ############ ICONS ##################
    const myicon = new L.Icon({
      iconUrl: require('./tesla.png'),
      shadowUrl: '',
      iconAnchor: [25, 50],
      popupAnchor: [0, -50],
      iconSize: new L.Point(50, 50),
    });

    const transInactive = new L.Icon({
      iconUrl: require('./transInactive.png'),
      shadowUrl: '',
      iconAnchor: [25, 50],
      popupAnchor: [0, -50],
      iconSize: new L.Point(50, 50),
    });

    const subIcon = new L.Icon({
      iconUrl: require('./pow.png'),
      shadowUrl: '',
      iconAnchor: [25, 50],
      popupAnchor: [0, -50],
      iconSize: new L.Point(50, 50),
    });

    const subInactive = new L.Icon({
      iconUrl: require('./subInactive.png'),
      shadowUrl: '',
      iconAnchor: [25, 50],
      popupAnchor: [0, -50],
      iconSize: new L.Point(50, 50),
    });

    const currentIcon = new L.Icon({
      iconUrl: require('./marker.png'),
      shadowUrl: '',
      iconAnchor: [20, 40],
      popupAnchor: [0, -40],
      iconSize: new L.Point(40, 40),
    });

    const countIcon = new L.Icon({
      iconUrl: require('./count.png'),
      shadowUrl: '',
      iconAnchor: [20, 40],
      popupAnchor: [0, -40],
      iconSize: new L.Point(40, 40),
    });

    const countInactive = new L.Icon({
      iconUrl: require('./countInactive.png'),
      shadowUrl: '',
      iconAnchor: [20, 40],
      popupAnchor: [0, -40],
      iconSize: new L.Point(40, 40),
    });
    // ############  ##################

    const allMarkers = this.state.transformer.map((ele, i) => (
      <Marker position={[ele.latitudeTransformator, ele.lengthTransformator]} key={i} icon={ele.is_active ? myicon : transInactive}>
        <Popup>
          <b>Transformer</b>: {ele.codeTransformator}<br></br>
            Lat: {ele.latitudeTransformator}<br></br>
            Lng: {ele.lengthTransformator}<br></br>
            Substation: <b>{ele.substationTransformator}</b><br></br>
          <center>
            <button className="removeBtn" onClick={() => this.removePoint(ele.codeTransformator, "transformer")}><b>Remove</b></button>
            <button className="inactiveBtn" onClick={() => this.inactiveActivePoint(ele.codeTransformator, ele.is_active, "transformer")}><b>{ele.is_active ? "Inactive" : "Active"}</b></button>
          </center>
        </Popup>
      </Marker>)
    );

    const allSubs = this.state.substations.map((ele, i) => (
      <Marker position={[ele.latitudeSubstation, ele.lengthSubstation]} key={i} icon={ele.is_active ? subIcon : subInactive}>
        <Popup>
          <b>Substation</b>: {ele.codeSubstation}<br></br>
            Lat: {ele.latitudeSubstation}<br></br>
            Lng: {ele.lengthSubstation}<br></br>
          <center>
            <button className="removeBtn" onClick={() => this.removePoint(ele.codeSubstation, "substations")}><b>Remove</b></button>
            <button className="inactiveBtn" onClick={() => this.inactiveActivePoint(ele.codeSubstation, ele.is_active, "substations")}><b>{ele.is_active ? "Inactive" : "Active"}</b></button>
          </center>
        </Popup>
      </Marker>)
    );

    const allCounters = this.state.counters.map((ele, i) => (
      <Marker position={[ele.latitudeCounter, ele.lengthCounter]} key={i} icon={ele.is_active ? countIcon : countInactive}>
        <Popup>
          <b>Counter</b>: {ele.codeCounter}<br></br>
            Lat: {ele.latitudeCounter}<br></br>
            Lng: {ele.lengthCounter}<br></br>
            Transformer: <b>{ele.transformatorCounter}</b><br></br>
          Address: <i>{ele.addressCounter}</i>
          <center>
            <button className="removeBtn" onClick={() => this.removePoint(ele.codeCounter, "counter")}><b>Remove</b></button>
            <button className="inactiveBtn" onClick={() => this.inactiveActivePoint(ele.codeCounter, ele.is_active, "counter")}><b>{ele.is_active ? "Inactive" : "Active"}</b></button>
          </center>
        </Popup>
      </Marker>)
    );

    const Tbtn = this.state.block ? <button onClick={() => this.newPoint("transformer")} className="newTrans">TR</button> : false;
    const Sbtn = this.state.blockSub ? <button onClick={() => this.newPoint("substations")} className="newSubs">SU</button> : false;
    const Cbtn = this.state.blockCo ? <button onClick={() => this.newPoint("counter")} className="newConts">CO</button> : false;

    const newMaker = Tbtn === Sbtn && Sbtn === Cbtn && Tbtn === Cbtn ?
      <p>Check Layer</p> :
      <div>{Sbtn}{Tbtn}{Cbtn}</div>;

    const modal = <div>
      <Modal md="7" isOpen={this.state.modal} toggle={this.closeToggle} className="danger">
        <ModalHeader toggle={this.closeToggle}>
          Insert Data
        </ModalHeader>
        <ModalBody>
          <Form onSubmit={this.handleSubmitCounterInfo}>
            <FormGroup>
              <Input onChange={this.handleCounterInfo} value={this.state.counterInfo.direccion} type="text" name="direccion" placeholder="Address" required />
              <Input onChange={this.handleCounterInfo} value={this.state.counterInfo.estrato} type="number" name="estrato" placeholder="Stratus" required />
              <Button color="success">
                Create
            </Button>
            </FormGroup>
          </Form>
        </ModalBody>
      </Modal>
    </div>

    return (
      <Map className="amapa" center={this.state.position} zoom={13} onClick={this.action} onoverlayadd={this.blockMarkers} onoverlayremove={this.blockMarkers}>
        {modal}
        <LayersControl position="topright">
          <LayersControl.BaseLayer name="BlackAndWhite">
            <TileLayer
              attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
              url="https://tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png"
            />
          </LayersControl.BaseLayer>
          <LayersControl.BaseLayer name="Mapnik" checked="true">
            <TileLayer
              attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
          </LayersControl.BaseLayer>
          <LayersControl.BaseLayer name="Transport">
            <TileLayer
              attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
              url="https://tile.memomaps.de/tilegen/{z}/{x}/{y}.png"
            />
          </LayersControl.BaseLayer>
          {/* End Layers */}

          <LayersControl.Overlay name="Transformers" checked="true" onClick={this.blockMarkers}>
            <LayerGroup>
              {allMarkers}
            </LayerGroup>
          </LayersControl.Overlay>

          <LayersControl.Overlay name="Substations" checked="true" onClick={this.blockMarkers}>
            <LayerGroup>
              {allSubs}
            </LayerGroup>
          </LayersControl.Overlay>

          <LayersControl.Overlay name="Counters" checked="true" onClick={this.blockMarkers}>
            <LayerGroup>
              {allCounters}
            </LayerGroup>
          </LayersControl.Overlay>

          <LayersControl.Overlay name="Feature group">
            <FeatureGroup color="red">
              <Popup>
                <span>Popup in FeatureGroup</span>
              </Popup>
              <Circle center={[3.4316, -76.5520]} radius={2000} />
            </FeatureGroup>
          </LayersControl.Overlay>
        </LayersControl>
        {/* Esto sirve si no se utilizan LayersControl.BaseLayer */}
        {/* <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution="&copy; <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
        /> */}
        <Marker position={this.state.movingMarker} icon={currentIcon}>
          <Popup>{newMaker}</Popup>
        </Marker>

      </Map>
    )
  }
}

export default TransformersMap;