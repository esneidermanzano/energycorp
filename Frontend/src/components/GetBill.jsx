import React from "react";

import logo from "logo.svg";

import { Link } from "react-router-dom";

import {
    Card,
    CardHeader,
    CardBody,
    CardFooter,
    CardTitle,
    Col, Form, FormGroup, Label, Input, Button, Alert, Table
} from "reactstrap";

import axios from "axios";

import counterpart from "counterpart";
import * as Tr from "react-translate-component";
import spanish from "../langs/spanish.js";
import english from "../langs/english.js";
import portuguese from "../langs/portuguese.js";

import { connect } from "react-redux";

counterpart.registerTranslations('en', english);
counterpart.registerTranslations('es', spanish);
counterpart.registerTranslations('po', portuguese);

class Start extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            contract: "",
            error: false,
            errorMsg: "",
            bills: [],
            sended: false,
            sendedMsg: ""
        }
    }

    handleInput = e => {
        this.setState({ contract: e.target.value });
    }

    handleSubmit = e => {
        e.preventDefault();
        if (this.state.contract !== "") {
            // console.log("dfd")
            // this.setState({ contract: "" })
            // window.open("https://energycorp.herokuapp.com/api/invoice/pdf/" + this.state.contract + "/");
            axios.post("https://energycorp.herokuapp.com/api/invoice/by-contract/", { contractNumber: parseInt(this.state.contract) })
                .then(res => {
                    var { error, find } = res.data;
                    if (error === true || find === false) {
                        // MENSAJE DE ERROR POR TRANSLATE
                        // console.log(message)
                        this.setState({ error: true, errorMsg: counterpart.translate('getBill.error') });
                        window.setTimeout(() => {
                            this.setState({ error: false, errorMsg: "" });
                        }, 2000);
                    } else {
                        this.setState({ bills: res.data.invoices })
                    }
                })
                .catch(err => {
                    console.log(err);
                })
        }
    }

    showPDF = (contract, bill) => {
        window.open("https://energycorp.herokuapp.com/api/invoice/pdf/" + contract + "/" + bill + "/");
    }

    sendMail = (contract, bill) => {
        this.setState({ sended: true, sendedMsg: counterpart.translate('getBill.enviando') });
        axios.get("https://energycorp.herokuapp.com/api/invoice/sendemail/" + contract + "/" + bill + "/")
            .then(res => {
                var { error, find } = res.data;
                if (error === true || find === false) {
                    // MENSAJE DE ERROR POR TRANSLATE
                    this.setState({ error: true, errorMsg: counterpart.translate('getBill.error') });
                    window.setTimeout(() => {
                        this.setState({ error: false, errorMsg: "" });
                    }, 2000);
                } else {
                    this.setState({ sendedMsg: counterpart.translate('getBill.exito') });
                    window.setTimeout(() => {
                        this.setState({ sended: false, errorMsg: "" });
                    }, 2000);
                }
            })
            .catch(err => {
                console.log(err);
            })
    }

    render() {

        const placeholderID = counterpart.translate('getBill.insert');

        const alert = (this.state.error) ? <Alert className="animated rubberBand" color="danger">
            <center>
                <h6>{this.state.errorMsg}</h6>
            </center>
        </Alert> : true;

        const alertMail = (this.state.sended) ? <Alert className="animated rubberBand" color="success">
            <center>
                <h6>{this.state.sendedMsg}</h6>
            </center>
        </Alert> : true;

        const bills = this.state.bills.length > 0 ?

            <Col md="8" id="login">
                <Table responsive borderless hover>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>ID</th>
                            <th><Tr content="getBill.contract" /></th>
                            <th><Tr content="getBill.billingDate" /></th>
                            <th><Tr content="getBill.deadDate" /></th>
                            <th><Tr content="getBill.state" /></th>
                            <th><Tr content="getBill.total" /></th>
                            <th><Tr content="getBill.mail" /></th>
                            <th><Tr content="getBill.show" /></th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            this.state.bills.map((ele, i) => (
                                <tr key={i}>
                                    <th>
                                        {i + 1}
                                    </th>
                                    <td>
                                        {ele.codeInvoice}
                                    </td>
                                    <td>
                                        {ele.contract}
                                    </td>
                                    <td>
                                        {ele.billingDate}
                                    </td>
                                    <td>
                                        {ele.deadDatePay}
                                    </td>
                                    <td>
                                        {ele.stateInvoice ?
                                            <Tr content="getBill.pago" /> :
                                            <Tr content="getBill.noPagado" />}
                                    </td>
                                    <td>
                                        ${ele.total.toFixed(2)} <br />
                                    </td>
                                    <td>
                                        <Button color="warning" onClick={() => this.sendMail(ele.contract, ele.codeInvoice)}>
                                            <i className="nc-icon nc-email-85" />
                                        </Button>
                                    </td>
                                    <td>
                                        <Button color="danger" onClick={() => this.showPDF(ele.contract, ele.codeInvoice)}>
                                            <i className="nc-icon nc-zoom-split" />
                                        </Button>
                                    </td>
                                </tr >
                            ))
                        }
                    </tbody>
                </Table>
            </Col> : true;


        return (
            <div>
                <Col md="4" id="login">
                    <Card>
                        {alert}
                        <CardHeader>
                            <center>
                                <img src={logo} width="80px" height="80px" alt="description"></img>
                                <CardTitle tag="h5">
                                    <Tr content="home.download" />
                                </CardTitle>
                            </center>

                        </CardHeader>
                        <CardBody>
                            <Form onSubmit={this.handleSubmit}>
                                <FormGroup>
                                    <Label for="exampleEmail">ID</Label>
                                    <Input onChange={this.handleInput} type="number" name="contract" id="exampleEmail" value={this.state.contract} placeholder={placeholderID} />
                                </FormGroup>
                                <center>
                                    <Button color="success">
                                        <Tr content="getBill.download" />
                                    </Button>
                                    <br />
                                    <Link to="/">
                                        <Tr content="getBill.home" />
                                    </Link>
                                </center>
                            </Form>
                        </CardBody>
                        <CardFooter>
                        </CardFooter>
                    </Card>
                </Col>
                {alertMail}
                {bills}
            </div>
        )
    }
}

const mapStateToProps = state => {
    counterpart.setLocale(state.language);
    return { lng: state.language }
}

const mapDispatchToProps = dispatch => ({});

export default connect(mapStateToProps, mapDispatchToProps)(Start);