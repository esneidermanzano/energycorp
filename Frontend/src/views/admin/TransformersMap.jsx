import React, { Component } from "react";
import { Map, Marker, Popup, TileLayer, LayersControl, FeatureGroup, Circle, LayerGroup } from 'react-leaflet';
import L from 'leaflet';
import axios from "axios";

class TransformersMap extends Component {
  constructor() {
    super();
    this.state = {
      position: [3.4516, -76.5320],
      movingMarker: [3.4616, -76.5000],
      transformer: [
        // {latitude:"0.3", length:"0.8", is_active: true}
        // {latitude:"3.4010161387921563", length:"-76.54030197567405", is_active: true},
        // {latitude:"3.4479673679891114", length:"-76.54137388830574", is_active: true},
        // {latitude:"3.4282618405834375", length:"-76.4944929034584", is_active: true}
      ],
      substations: [
        // {latitude:"3.4203795158094206", length:"-76.55888986066627", is_active: true},
        // {latitude:"3.431860271609247", length:"-76.52007996112233", is_active: true}
      ],
      block: true,
      blockSub: true
    };
  }

  action = e => {
    this.setState({ movingMarker: [e.latlng.lat, e.latlng.lng] });
  }

  newPoint = (type) => {
    var obj;
    if (type === "transformer") {

      obj = {
        latitude: this.state.movingMarker[0].toString(),
        length: this.state.movingMarker[1].toString(),
        is_active: true,
        substation: 1
      };

      axios.post("https://energycorp.herokuapp.com/api/energytransfers/transformator/create/", obj)
        .then(res => {
          this.setState({ transformer: [...this.state.transformer, obj] });
        })
        .catch(err => {
          console.log(err);
        })

    } else {
      obj = {
        latitude: this.state.movingMarker[0].toString(),
        length: this.state.movingMarker[1].toString(),
        is_active: true
      };

      axios.post("https://energycorp.herokuapp.com/api/energytransfers/substation/create/", obj)
        .then(res => {
          this.setState({ substations: [...this.state.substations, obj] });
        })
        .catch(err => {
          console.log(err);
        })

    }
  }

  removePoint = (key, type) => {
    var copy;
    if (type === "transformer") {

      // axios.post("https://energycorp.herokuapp.com/api/energytransfers/transformator/inactivate/"+(key+1))
      //   .then(res => {

      //   })
      //   .catch(err => {
      //     console.log(err);
      //   })

      copy = [...this.state.transformer];
      copy.splice(key, 1);
      this.setState({ transformer: copy });
    } else {
      copy = [...this.state.substations];
      copy.splice(key, 1);
      this.setState({ substations: copy });
    }
  }

  inactiveActivePoint = (key, type) => {
    var copy;
    var k; 
    if (type === "transformer") {
      k = key+1;
      axios.patch("https://energycorp.herokuapp.com/api/energytransfers/transformator/inactivate/"+k+"/", {"is_active": !this.state.transformer[key].is_active })
        .then(res => {
          copy = [...this.state.transformer];
          copy[key].is_active = !copy[key].is_active;
          this.setState({ transformer: copy });
        })
        .catch(err => {
          console.log(err);
        })

    }else{
      k = key+1;
      axios.patch("https://energycorp.herokuapp.com/api/energytransfers/substation/inactivate/"+k+"/", {"is_active": !this.state.substations[key].is_active })
        .then(res => {
          copy = [...this.state.substations];
          copy[key].is_active = !copy[key].is_active;
          this.setState({ substations: copy });
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
    }
  }

  async componentDidMount() {
    const res = await fetch('https://energycorp.herokuapp.com/api/energytransfers/transformator');
    const res2 = await fetch('https://energycorp.herokuapp.com/api/energytransfers/substation/');

    const data = await res.json();
    const data2 = await res2.json();

    var ts = [];
    var sb = [];

    for (let i = 0; i < data.length; i++) {
      ts.push(data[i]);
    }

    for (let i = 0; i < data2.length; i++) {
      sb.push(data2[i]);
    }

    this.setState({ transformer: ts, substations: sb });
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
    // ############  ##################

    const allMarkers = this.state.transformer.map((ele, i) => (
      <Marker position={[ele.latitude, ele.length]} key={i} icon={ele.is_active ? myicon : transInactive}>
        <Popup>
          {/* <b>Transformer</b>: {i + 1}<br></br> */}
            Lat: {ele.latitude}<br></br>
            Lng: {ele.length}<br></br>
          <center>
            <button className="removeBtn" onClick={() => this.removePoint(i, "transformer")}><b>Remove</b></button>
            <button className="inactiveBtn" onClick={() => this.inactiveActivePoint(i, "transformer")}><b>{ele.is_active ? "Inactive" : "Active"}</b></button>
          </center>
        </Popup>
      </Marker>)
    );

    const allSubs = this.state.substations.map((ele, i) => (
      <Marker position={[ele.latitude, ele.length]} key={i} icon={ele.is_active ? subIcon : subInactive}>
        <Popup>
          {/* <b>Substation</b>: {i + 1}<br></br> */}
            Lat: {ele.latitude}<br></br>
            Lng: {ele.length}<br></br>
          <center>
            <button className="removeBtn" onClick={() => this.removePoint(i, "substations")}><b>Remove</b></button>
            <button className="inactiveBtn" onClick={() => this.inactiveActivePoint(i, "substations")}><b>{ele.is_active ? "Inactive" : "Active"}</b></button>
          </center>
        </Popup>
      </Marker>)
    );

    const Tbtn = this.state.block ? <button onClick={() => this.newPoint("transformer")} className="newTrans">TR</button> : false;
    const Sbtn = this.state.blockSub ? <button onClick={() => this.newPoint("substations")} className="newSubs">SU</button> : false;
    const newMaker = Tbtn === Sbtn ? <p>Check Layer</p> : <div>{Tbtn}{Sbtn}</div>;

    return (
      <Map className="amapa" center={this.state.position} zoom={13} onClick={this.action} onoverlayadd={this.blockMarkers} onoverlayremove={this.blockMarkers}>
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