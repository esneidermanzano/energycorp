import React from "react";

import {
    CardTitle,
    Col, Form, FormGroup, Input, Button, Table,
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

class ViewPayments extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            contract: "",
            error: false,
            errorMsg: "",
            payments: [],
            sended: false,
            sendedMsg: ""
        }
    }

    handleInput = e => {
        this.setState({ [e.target.name]: e.target.value});
    }

    handleSubmit = e => {
        e.preventDefault();
        if (this.state.contract !== "") {
            axios.get("https://energycorp.herokuapp.com/api/pay/payment/bycontract/" + this.state.contract)
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
                        this.setState({ payments: res.data })
                    }
                })
                .catch(err => {
                    console.log(err);
                })
         }        
    } 

    render() {

        const placeholderID = counterpart.translate('getBill.insert');
        const payments = this.state.payments.length > 0 ?

            <Col md="11" id="login">
                <Table responsive borderless hover>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th><Tr content="getBill.contract" /></th>
                            <th><Tr content="getBill.billingDate" /></th>
                            <th><Tr content="getBill.deadDate" /></th>
                            <th><Tr content="getBill.vPayment" /></th>
                            <th><Tr content="getBill.total" /></th>
                            <th><Tr content="clientForm.address" /></th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            this.state.payments.map((p, i) => (
                                <tr key={i}>
                                    <th>
                                        {i + 1}
                                    </th>
                                    <td>
                                        {p.facturaPayment.contract}
                                    </td>
                                    <td>
                                        {p.facturaPayment.billingDate}
                                    </td>
                                    <td>
                                        {p.facturaPayment.deadDatePay}
                                    </td>
                                    <td>
                                        ${p.valuePayment.toFixed(2)} <br />
                                    </td>
                                    <td>
                                        ${p.facturaPayment.total.toFixed(2)} <br />
                                    </td>
                                    <td>
                                        {p.facturaPayment.address}
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
                                    <Tr content="home.consult" />
                                </CardTitle>
                            </center>
                            <br />
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
                {payments}
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

export default connect(mapStateToProps, mapDispatchToProps)(ViewPayments);