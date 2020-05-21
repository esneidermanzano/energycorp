import React from "react";

import counterpart from "counterpart";
// import * as Tr from "react-translate-component";
import spanish from "../../langs/spanish.js";
import english from "../../langs/english.js";
import portuguese from "../../langs/portuguese.js";

import { connect } from "react-redux";

// import {
//     Card,
//     CardBody,
//     Row,
//     Col, FormGroup, Input, Button, Table,
//     Modal, ModalHeader, ModalBody
// } from "reactstrap";

counterpart.registerTranslations('en', english);
counterpart.registerTranslations('es', spanish);
counterpart.registerTranslations('po', portuguese);

class Payments extends React.Component {
    constructor(props) {
        super(props);
        this.state = { 
        }
    }

    handleInput = e => {
        this.setState({
            [e.target.name]: e.target.value
        });
    }


    async componentDidMount() {
    }

    render() {
        return (
            <div className="content">
                <h1>Payment</h1>
            </div>
        )
    }
};

const mapStateToProps = state => {
    counterpart.setLocale(state.language);
    return { lng: state.language }
}

const mapDispatchToProps = dispatch => ({});

export default connect(mapStateToProps, mapDispatchToProps)(Payments);