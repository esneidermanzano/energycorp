import React from "react";

import counterpart from "counterpart";
import * as Tr from "react-translate-component";
import spanish from "../../langs/spanish.js";
import english from "../../langs/english.js";
import portuguese from "../../langs/portuguese.js";

import { connect } from "react-redux";

// reactstrap components
import {
    Row, Col, Form, FormGroup, Label, Input, Button
} from "reactstrap";

counterpart.registerTranslations('en', english);
counterpart.registerTranslations('es', spanish);
counterpart.registerTranslations('po', portuguese);

class CreateClientForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = this.props.user || {
            // id_user: "",
            // name: "",
            // email: "",
            // password: "loquendo",
            // phone: "",
            // address: "",
            // neighborhood: "",
            // stratus: null,
            // is_active: true,
            // is_staff: false,
            // is_superuser: false,
            // client: {
            //     type_client: 1,
            //     interes_mora: null,
            //     cycle: "",
            //     contrat_number: null,
            //     financial_state: "mora",
            //     billing: "",
            // }
            type_client: 1,
            interes_mora: null,
            cycle: "",
            contrat_number: null,
            financial_state: "mora",
            billing: "",
            user: {
                id_user: "",
                name: "",
                email: "",
                password: "loquendo",
                phone: "",
                address: "",
                neighborhood: "",
                stratus: null,
                is_active: true,
                is_staff: false,
                is_superuser: false,
            }

        }
    }

    handleInputClient = e => {

        var val = e.target.value;

        // Pre Process ////////////////////////
        if (e.target.name === "type_client") {
            val = parseInt(val);
        } else if (e.target.name === "interes_mora") {
            val = parseFloat(val);
        } else if (e.target.name === "contrat_number") {
            val = parseInt(val);
        }
        ////////////////////////////////////////////////

        this.setState({
            [e.target.name]: val
        });
    }

    handleInput = e => {

        var { user } = { ...this.state };

        var val = e.target.value;

        // Pre Process ////////////////////////
        if (e.target.name === "is_active") {
            if (val === "Activo") {
                val = true;
            } else {
                val = false;
            }
        } else if (e.target.name === "stratus") {
            val = parseInt(val);
        }
        ////////////////////////////////////////////////

        user[e.target.name] = val;

        this.setState({
            user: user
        });

    }

    cleanForm = () => {
        document.getElementById("form").reset();
    }

    handleSubmit = e => {
        e.preventDefault();
        
        this.props.submitAction(this.state);

        this.cleanForm();

        this.setState({
            type_client: 1,
            interes_mora: null,
            cycle: "",
            contrat_number: null,
            financial_state: "mora",
            billing: "",
            user: {
                id_user: "",
                name: "",
                email: "",
                password: "loquendo",
                phone: "",
                address: "",
                neighborhood: "",
                stratus: null,
                is_active: true,
                is_staff: false,
                is_superuser: false,
            }
        });
    }

    render() {

        const addBtn = (!this.props.user) ? 
            <Button color="warning">
                 <Tr content="clientForm.add"/>
            </Button> : 
            <Button color="warning">
                 <Tr content="clientForm.edit"/>
            </Button>;

        const showStateAttr = this.props.editMode ? <div> 
                <Label for="">
                    <Tr content="clientForm.state"/>
                </Label>
            <select onChange={this.handleInput} value={this.state.user.is_active} className="form-control" name="is_active" required>
                <Tr content="clientForm.active" component="option"/>
                <Tr content="clientForm.inactive" component="option"/>
            </select>
        </div> : true

        const placeholderRate = counterpart.translate('clientForm.rate');
        const placeholderCycle = counterpart.translate('clientForm.cycle');
        const placeholderContractN = counterpart.translate('clientForm.contractN');
        const placeholderBilling = counterpart.translate('clientForm.billing');
        const placeholderName = counterpart.translate('clientForm.name');
        const placeholderAddress = counterpart.translate('clientForm.address');
        const placeholderNeighborhood = counterpart.translate('clientForm.neighborhood');
        const placeholderPhone = counterpart.translate('clientForm.phone');
        const placeholderStratum = counterpart.translate('clientForm.stratum');

        const aditional =
            <div>
                <center style={{ marginTop: "2em" }}>
                    <Tr content="clientForm.aditionalInfo"/>
                </center>

                <Row>
                    <Col>
                        <Label for="">
                            <Tr content="clientForm.type"/>
                        </Label>
                        <select onChange={this.handleInputClient} value={this.state.type_client} className="form-control" name="type_client" required>
                            <Tr content="clientForm.natural" component="option" value="1"/>
                            <Tr content="clientForm.legal" component="option" value="2"/>
                        </select>
                    </Col>
                    <Col>
                        <Label for="">
                            <Tr content="clientForm.rate"/>
                        </Label>
                        <Input onChange={this.handleInputClient} value={this.state.interes_mora} type="number" step="0.01" name="interes_mora" placeholder={placeholderRate} required />
                    </Col>
                </Row>

                <Row>
                    <Col>
                        <Label for="">
                            <Tr content="clientForm.cycle"/>
                        </Label>
                        <Input onChange={this.handleInputClient} value={this.state.cycle} type="number" name="cycle" placeholder={placeholderCycle} required />
                    </Col>
                    <Col>
                        <Label for="">
                            <Tr content="clientForm.contractN"/>
                        </Label>
                        <Input onChange={this.handleInputClient} value={this.state.contrat_number} type="text" name="contrat_number" placeholder={placeholderContractN} required />
                    </Col>
                </Row>

                <Row>
                    <Col>
                        <Label for="">
                            <Tr content="clientForm.billing"/>
                        </Label>
                        <Input onChange={this.handleInputClient} value={this.state.billing} type="number" name="billing" placeholder={placeholderBilling} required />
                    </Col>
                    <Col>
                        <Label for="">
                            <Tr content="clientForm.stateF"/>
                        </Label>
                        <select onChange={this.handleInputClient} value={this.state.financial_state} className="form-control" name="financial_state" required>
                            <Tr content="clientForm.mora" component="option" value="Mora"/>
                            <Tr content="clientForm.noMora" component="option" value="No Mora"/>
                        </select>
                    </Col>
                </Row>

            </div>

        return (
            <Form id="form" onSubmit={this.handleSubmit}>
                <FormGroup>
                    <div>
                        <Row>
                            <Col>
                                <Label for="">ID</Label>
                                <Input onChange={this.handleInput} value={this.state.user.id_user} type="number" name="id_user" placeholder="ID" required />
                            </Col>
                        </Row>

                        <Row>
                            <Col>
                                <Label for="">
                                    <Tr content="clientForm.name"/>
                                </Label>
                                <Input onChange={this.handleInput} value={this.state.user.name} type="text" name="name" placeholder={placeholderName} required />
                            </Col>
                        </Row>
                        <Label for="">Email</Label>
                        <Input onChange={this.handleInput} value={this.state.user.email} type="email" name="email" placeholder="Email" required />

                        <Row>
                            <Col>
                                <Label for="">
                                    <Tr content="clientForm.address"/>
                                </Label>
                                <Input onChange={this.handleInput} value={this.state.user.address} type="text" name="address" placeholder={placeholderAddress} required />
                            </Col>
                            <Col>
                                <Label for="">
                                    <Tr content="clientForm.neighborhood"/>
                                </Label>
                                <Input onChange={this.handleInput} value={this.state.user.neighborhood} type="text" name="neighborhood" placeholder={placeholderNeighborhood} required />
                            </Col>
                            <Col>
                                <Label for="">
                                    <Tr content="clientForm.stratum"/>
                                </Label>
                                <Input onChange={this.handleInput} value={this.state.user.stratus} type="number" name="stratus" placeholder={placeholderStratum} required />
                            </Col>
                        </Row>

                        <Label for="">
                            <Tr content="clientForm.phone"/>
                        </Label>
                        <Input onChange={this.handleInput} value={this.state.user.phone} type="number" name="phone" placeholder={placeholderPhone} required />
                        {showStateAttr}
                        {aditional}
                    </div>
                </FormGroup>
                {addBtn}
            </Form>
        )
    }
};

const mapStateToProps = state => {
    counterpart.setLocale(state.language);
    return { lng: state.language }
}

const mapDispatchToProps = dispatch => ({});

export default connect(mapStateToProps, mapDispatchToProps)(CreateClientForm);