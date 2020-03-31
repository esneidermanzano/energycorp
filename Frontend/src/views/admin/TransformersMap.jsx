import React, { Component } from "react";
import { Map, Marker, Popup, TileLayer, LayersControl, FeatureGroup, Circle, LayerGroup } from 'react-leaflet';
import L from 'leaflet';

class TransformersMap extends Component {
  constructor() {
    super();
    this.state = {
      position: [3.4516, -76.5320],
      movingMarker: [3.4616, -76.5000],
      pos: [
        [3.4010161387921563, -76.54030197567405],
        [3.4479673679891114, -76.54137388830574],
        [3.4282618405834375, -76.4944929034584]
      ],
      posSubs: [
        [3.4203795158094206, -76.55888986066627],
        [3.431860271609247, -76.52007996112233]
      ],
      block: true,
      blockSub: true
    };
  }

  action = e => {
    this.setState({ movingMarker: [e.latlng.lat, e.latlng.lng] });
  }

  newPoint = (type) => {
    if (type === "pos") {
      this.setState({ pos: [...this.state.pos, this.state.movingMarker] });
    } else {
      this.setState({ posSubs: [...this.state.posSubs, this.state.movingMarker] });
    }
  }

  removePoint = (key, type) => {
      var copy;
    if (type === "pos") {
      copy = [...this.state.pos];
      copy.splice(key, 1);
      this.setState({ pos: copy });
    } else {
      copy = [...this.state.posSubs];
      copy.splice(key, 1);
      this.setState({ posSubs: copy });
    }

  }

  blockMarkers = e => {
    if (e.name === "All markers") {
      this.setState({ block: !this.state.block });
    } else if (e.name === "Substations") {
      this.setState({ blockSub: !this.state.blockSub });
    }
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

    const subIcon = new L.Icon({
      iconUrl: require('./pow.png'),
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

    const allMarkers = this.state.pos.map((ele, i) => (
      <Marker position={ele} key={i} icon={myicon}>
        <Popup>
          <b>Transformer</b>: {i+1}<br></br>
            Lat: {ele[0]}<br></br>
            Lng: {ele[1]}<br></br>
            <center>
              <button color="danger" className="removeBtn" onClick={() => this.removePoint(i, "pos")}><b>Remove</b></button>
            </center>
        </Popup>
      </Marker>)
    );

    const allSubs = this.state.posSubs.map((ele, i) => (
      <Marker position={ele} key={i} icon={subIcon}>
        <Popup>
            <b>Substation</b>: {i+1}<br></br>
            Lat: {ele[0]}<br></br>
            Lng: {ele[1]}<br></br>
            <center>
              <button color="danger" className="removeBtn" onClick={() => this.removePoint(i, "posSubs")}><b>Remove</b></button>
            </center>
        </Popup>
      </Marker>)
    );

    const Tbtn = this.state.block ? <button onClick={() => this.newPoint("pos")} className="newTrans">TR</button> : false;
    const Sbtn = this.state.blockSub ? <button onClick={() => this.newPoint("posSubs")} className="newSubs">SU</button> : false ;
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

          <LayersControl.Overlay name="All markers" checked="true" onClick={this.blockMarkers}>
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