/*!

=========================================================
* Paper Dashboard React - v1.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/paper-dashboard-react
* Copyright 2019 Creative Tim (https://www.creative-tim.com)

* Licensed under MIT (https://github.com/creativetimofficial/paper-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React from "react";
// javascript plugin used to create scrollbars on windows
import PerfectScrollbar from "perfect-scrollbar";
import { Route, Switch, Redirect } from "react-router-dom";

import DemoNavbar from "components/Navbars/DemoNavbar.jsx";
import Footer from "components/Footer/Footer.jsx";
import Sidebar from "components/Sidebar/Sidebar.jsx";

// import routes from "routes/routes.js";

var ps;

class DashLayout extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      backgroundColor: "green",
      activeColor: "warning"
    };
    this.mainPanel = React.createRef();
  }
  componentDidMount() {
    if (navigator.platform.indexOf("Win") > -1) {
      ps = new PerfectScrollbar(this.mainPanel.current);
      document.body.classList.toggle("perfect-scrollbar-on");
    }
  }
  componentWillUnmount() {
    if (navigator.platform.indexOf("Win") > -1) {
      ps.destroy();
      document.body.classList.toggle("perfect-scrollbar-on");
    }
  }
  componentDidUpdate(e) {
    if (e.history.action === "PUSH") {
      this.mainPanel.current.scrollTop = 0;
      document.scrollingElement.scrollTop = 0;
    }
  }
  handleActiveClick = color => {
    this.setState({ activeColor: color });
  };
  handleBgClick = color => {
    this.setState({ backgroundColor: color });
  };

  getActiveColor = () => {
    const la = this.props.routes[0].layout;
    if (la === "/admin") {
      return "success";
    }else if(la === "/operator"){
      return "warning";
    }else{
      return "info";
    }
  }

  render() {
    return (
      <div className="wrapper animated fadeIn slow">
        <Sidebar
          {...this.props}
          routes={this.props.routes}
          bgColor={this.state.backgroundColor}
          activeColor={this.getActiveColor()}
        />
        <div className="main-panel animated zoomInDown" ref={this.mainPanel}>
          <DemoNavbar {...this.props} routes={this.props.routes} />
          <Switch>
            {this.props.routes.map((prop, key) => {
              return (
                <Route
                  path={prop.layout + prop.path}
                  component={prop.component}
                  key={key}
                />
              );
            })}
            <Redirect to={this.props.routes[0].layout + this.props.routes[0].path} />
          </Switch>
          <Footer fluid />
        </div>
      </div>
    );
  }
}

export default DashLayout;
