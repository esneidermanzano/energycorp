import React from "react";
import DemoNavbar from "components/Navbars/DemoNavbar.jsx";

import { Link } from "react-router-dom";

class Start extends React.Component {
    constructor(props) {
        super(props);
        this.state = {}
    }

    render() {
        return (
            <div>
                <DemoNavbar {...this.props} />
                <div className="contentStart">
                    <center>
                        <h1>El Mejor Servicio a tu Alcance</h1>
                        <img width="744" height="490" src="https://www.mercapava.com.co/wp-content/uploads/2016/10/Tip-5.jpg" alt="description"></img>
                        <br></br>
                        <Link className="btn btn-danger" to="/getBill">Download your Bill!</Link>
                    </center>
                </div>
            </div>
        )
    }
}

export default Start;