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
import { Link } from "react-router-dom";
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  Dropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem,
  Container,
  Button, Row, Col
} from "reactstrap";

import auth from "components/auth/auth.js";


import { connect } from "react-redux";


import en_icon from "./england_icon.png";
import es_icon from "./spain_icon.png";
import po_icon from "./portuguese_icon.png";



// import routes from "routes/routes.js";

class Header extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isOpen: false,
      dropdownOpen: false,
      color: "transparent"
    };
    this.toggle = this.toggle.bind(this);
    this.dropdownToggle = this.dropdownToggle.bind(this);
    this.sidebarToggle = React.createRef();
  }

  toggle() {
    if (this.state.isOpen) {
      this.setState({
        color: "transparent"
      });
    } else {
      this.setState({
        color: "dark"
      });
    }
    this.setState({
      isOpen: !this.state.isOpen
    });
  }
  dropdownToggle(e) {
    this.setState({
      dropdownOpen: !this.state.dropdownOpen
    });
  }
  getBrand() {
    let brandName = "energyCorp";
    if (this.props.routes !== undefined) {
      this.props.routes.map((prop, key) => {
        if (window.location.href.indexOf(prop.layout + prop.path) !== -1) {
          brandName = prop.name;
        }
        return null;
      });
    }

    return brandName;
  }
  openSidebar() {
    document.documentElement.classList.toggle("nav-open");
    this.sidebarToggle.current.classList.toggle("toggled");
  }
  // function that adds color dark/transparent to the navbar on resize (this is for the collapse)
  updateColor() {
    if (window.innerWidth < 993 && this.state.isOpen) {
      this.setState({
        color: "dark"
      });
    } else {
      this.setState({
        color: "transparent"
      });
    }
  }
  componentDidMount() {
    window.addEventListener("resize", this.updateColor.bind(this));
  }
  componentDidUpdate(e) {
    if (
      window.innerWidth < 993 &&
      e.history.location.pathname !== e.location.pathname &&
      document.documentElement.className.indexOf("nav-open") !== -1
    ) {
      document.documentElement.classList.toggle("nav-open");
      this.sidebarToggle.current.classList.toggle("toggled");
    }
  }
  render() {

    const loggedInBtn = this.props.loggedInBtn ?
      <Button onClick={() => {
        auth.logout(() => { this.props.history.push("/login") })
      }}>Logout</Button>
      :
      <Link className="btn" to="/login">Login</Link>

    return (
      // add or remove classes depending if we are on full-screen-maps page or not
      <Navbar
        color={
          this.props.location.pathname.indexOf("full-screen-maps") !== -1
            ? "dark"
            : this.state.color
        }
        expand="lg"
        className={
          this.props.location.pathname.indexOf("full-screen-maps") !== -1
            ? "navbar-absolute fixed-top"
            : "navbar-absolute fixed-top " +
            (this.state.color === "transparent" ? "navbar-transparent " : "")
        }
      >
        <Container fluid>
          <div className="navbar-wrapper">
            <div className="navbar-toggle">
              <button
                type="button"
                ref={this.sidebarToggle}
                className="navbar-toggler"
                onClick={() => this.openSidebar()}
              >
                <span className="navbar-toggler-bar bar1" />
                <span className="navbar-toggler-bar bar2" />
                <span className="navbar-toggler-bar bar3" />
              </button>
            </div>
            <NavbarBrand href="/">{this.getBrand()}</NavbarBrand>
          </div>
          <NavbarToggler onClick={this.toggle}>
            <span className="navbar-toggler-bar navbar-kebab" />
            <span className="navbar-toggler-bar navbar-kebab" />
            <span className="navbar-toggler-bar navbar-kebab" />
          </NavbarToggler>
          <Collapse
            isOpen={this.state.isOpen}
            navbar
            className="justify-content-end"
          >
            {/* <form>
              <InputGroup className="no-border">
                <Input placeholder="Search..." />
                <InputGroupAddon addonType="append">
                  <InputGroupText>
                    <i className="nc-icon nc-zoom-split" />
                  </InputGroupText>
                </InputGroupAddon>
              </InputGroup>
            </form> */}
            <Nav navbar>
              {/* <NavItem>
                <Link to="#pablo" className="nav-link btn-magnify">
                  <i className="nc-icon nc-layout-11" />
                  <p>
                    <span className="d-lg-none d-md-block">Stats</span>
                  </p>
                </Link>
              </NavItem> */}
              <Dropdown
                nav
                isOpen={this.state.dropdownOpen}
                toggle={e => this.dropdownToggle(e)}
              >
                <DropdownToggle caret nav>
                  <i className="nc-icon nc-caps-small" />
                  <p>
                    <span className="d-lg-none d-md-block">Some Actions</span>
                  </p>
                </DropdownToggle>
                <DropdownMenu right>
                  <DropdownItem tag="a"  onClick={() => this.props.changeLng('en')}>
                    <Row>
                      <Col>
                        <img src={en_icon} alt="" width="30px" height="30px" />
                      </Col>
                      <Col>
                        English
                      </Col>
                    </Row>
                  </DropdownItem>
                  <DropdownItem tag="a" onClick={() => this.props.changeLng('es')}>
                    <Row>
                      <Col>
                        <img src={es_icon} alt="" width="30px" height="30px" />
                      </Col>
                      <Col>
                        Spanish
                      </Col>
                    </Row>
                  </DropdownItem>
                  <DropdownItem tag="a" onClick={() => this.props.changeLng('po')}>
                    <Row>
                      <Col>
                        <img src={po_icon} alt="" width="30px" height="30px" />
                      </Col>
                      <Col sm="7">
                        Portuguese
                      </Col>
                    </Row>
                  </DropdownItem>
                </DropdownMenu>
              </Dropdown>
              {/* <NavItem> */}
                {loggedInBtn}
              {/* </NavItem> */}
            </Nav>
          </Collapse>
        </Container>
      </Navbar>
    );
  }
}

const mapStateToProps = state => ({})

const mapDispatchToProps = dispatch => ({
  changeLng(lan) {
    dispatch({
      type: "CHANGE_LAN",
      language: lan
    })
  }
});

export default connect(mapStateToProps, mapDispatchToProps)(Header);
