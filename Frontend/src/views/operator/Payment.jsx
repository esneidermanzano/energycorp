import React from "react";

import auth from "components/auth/auth.js";

import {
    CardTitle,
    Col, Form, FormGroup, Input, Button, Alert, Table
} from "reactstrap";

import axios from "axios";

import counterpart from "counterpart";
import * as Tr from "react-translate-component";
import spanish from "../../langs/spanish.js";
import english from "../../langs/english.js";
import portuguese from "../../langs/portuguese.js";

import { connect } from "react-redux";

counterpart.registerTranslations('en', english);
counterpart.registerTranslations('es', spanish);
counterpart.registerTranslations('po', portuguese);

class Payment extends React.Component {
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

    pay = (value, bill, worker) => {
        const msg = {
            payment: {
                valuePayment: value,
                facturaPayment: bill
            },
            workerPayment: worker
        }    

        console.log(msg);

        axios.post("https://energycorp.herokuapp.com/api/pay/directpayment/create/", msg)
            .then(res => {
                alert(counterpart.translate('createClient.exito'));
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
                            <th><Tr content="getBill.pay" /></th>
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
                                        {ele.stateInvoice ? "" :
                                        <Button color="success" onClick={() => 
                                            this.pay(ele.total,ele.codeInvoice,auth.getObj().id)}>
                                            <i className="nc-icon nc-money-coins" />
                                        </Button>}
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
                            <center>
                                <CardTitle tag="h5">
                                    <Tr content="home.pay" />
                                </CardTitle>
                            </center>
                            <Form onSubmit={this.handleSubmit}>
                                <FormGroup>
                                    <Input onChange={this.handleInput} type="number" name="contract" id="exampleEmail" value={this.state.contract} placeholder={placeholderID} />
                                </FormGroup>
                                <center>
                                    <Button color="success">
                                        <Tr content="getBill.consult" />
                                    </Button>
                                </center>
                            </Form>
                </Col>
                {alertMail}
                {bills}
                <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
            </div>
        )
    }
}

const mapStateToProps = state => {
    counterpart.setLocale(state.language);
    return { lng: state.language }
}

const mapDispatchToProps = dispatch => ({});

export default connect(mapStateToProps, mapDispatchToProps)(Payment);