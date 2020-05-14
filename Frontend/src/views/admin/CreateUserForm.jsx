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

class CreateUserForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = this.props.user || {
            user_type: 2,
            id_user: '',
            name: '',
            email: '',
            password: 'loquendo',
            phone: '',
            address: '',
            neighborhood: '',
            stratus: '',
            is_active: true,
            is_staff: true,
            is_superuser: false
        }
    }

    handleInput = e => {

        var val = e.target.value;

        if (e.target.name === "is_active") {
            if (val === "Activo") {
                val = true;
            } else {
                val = false;
            }
        }else if (e.target.name === "stratus") {
            val = parseInt(val);
        }else if (e.target.name === "user_type") {
            val = parseInt(val);
        }

        this.setState({
            [e.target.name]: val
        });
    }

    cleanForm = () => {
        document.getElementById("form").reset();
    }

    handleSubmit = e => {
        e.preventDefault();

        var theState;

        theState = { ...this.state };
        delete theState.client;
        this.props.submitAction(theState);

        this.cleanForm();

        this.setState({
            user_type: 'operador',
            id_user: '',
            name: '',
            email: '',
            password: 'loquendo',
            phone: '',
            address: '',
            neighborhood: '',
            stratus: '',
            is_active: true,
            is_staff: true,
            is_superuser: false
        });
    }

    render() {

        const addBtn = (!this.props.user) ? 
        <Button color="success">
            <Tr content="clientForm.add"/>
        </Button> : <Button color="success">
            <Tr content="clientForm.edit"/>
        </Button>;

        const showStateAttr = this.props.editMode ? <div> 
                <Label for="">
                    <Tr content="clientForm.state"/>
                </Label>
            <select onChange={this.handleInput} value={this.state.is_active} className="form-control" name="is_active" required>
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

        const aditional = (this.state.user_type === 'Cliente') ? <div>
            <center style={{ marginTop: "2em" }}>
                <Tr content="clientForm.aditionalInfo"/>
            </center>

            <Row>
                <Col>
                    <Label for="">
                        <Tr content="clientForm.type"/>
                    </Label>
                    <select onChange={this.handleInputClient} value={this.state.client.type_client} className="form-control" name="type_client" required>
                        <Tr content="clientForm.natural" component="option"/>
                        <Tr content="clientForm.legal" component="option"/>
                    </select>
                </Col>
                <Col>
                    <Label for="">
                        <Tr content="clientForm.rate"/>
                    </Label>
                    <Input onChange={this.handleInputClient} value={this.state.client.interes_mora} type="number" name="interes_mora" placeholder={placeholderRate} required />
                </Col>
            </Row>

            <Row>
                <Col>
                    <Label for="">
                        <Tr content="clientForm.cycle"/>
                    </Label>
                    <Input onChange={this.handleInputClient} value={this.state.client.cycle} type="number" name="cycle" placeholder={placeholderCycle} required />
                </Col>
                <Col>
                    <Label for="">
                        <Tr content="clientForm.contractN"/>
                    </Label>
                    <Input onChange={this.handleInputClient} value={this.state.client.contrat_number} type="text" name="contrat_number" placeholder={placeholderContractN} required />
                </Col>
            </Row>

            <Row>
                <Col>
                    <Label for="">
                        <Tr content="clientForm.billing"/>
                    </Label>
                    <Input onChange={this.handleInputClient} value={this.state.client.billing} type="number" name="billing" placeholder={placeholderBilling} required />
                </Col>
                <Col>
                    <Label for="">
                        <Tr content="clientForm.stateF"/>
                    </Label>
                    <select onChange={this.handleInputClient} value={this.state.client.financial_state} className="form-control" name="financial_state" required>
                        <Tr content="clientForm.mora" component="option"/>
                        <Tr content="clientForm.noMora" component="option"/>
                    </select>
                </Col>
            </Row>

        </div> : true

        return (
            <Form id="form" onSubmit={this.handleSubmit}>
                <FormGroup>
                    <div>
                        <Label for="">
                            <Tr content="createUser.userType"/>
                        </Label>
                        <select onChange={this.handleInput} value={this.state.user_type} className="form-control" name="user_type" required>
                            <Tr content="createUser.operator" component="option"/>
                            <Tr content="createUser.manager" component="option"/>
                        </select>
                        <Row>
                            <Col>
                                <Label for="">ID</Label>
                                <Input onChange={this.handleInput} value={this.state.id_user} type="number" name="id_user" placeholder="ID" required />
                            </Col>
                        </Row>

                        <Row>
                            <Col>
                                <Label for="">
                                    <Tr content="clientForm.name"/>
                                </Label>
                                <Input onChange={this.handleInput} value={this.state.name} type="text" name="name" placeholder={placeholderName} required />
                            </Col>
                        </Row>
                        <Label for="">Email</Label>
                        <Input onChange={this.handleInput} value={this.state.email} type="email" name="email" placeholder="Email" required />

                        <Row>
                            <Col>
                                <Label for="">
                                    <Tr content="clientForm.address"/>
                                </Label>
                                <Input onChange={this.handleInput} value={this.state.address} type="text" name="address" placeholder={placeholderAddress} required />
                            </Col>
                            <Col>
                                <Label for="">
                                    <Tr content="clientForm.neighborhood"/>
                                </Label>
                                <Input onChange={this.handleInput} value={this.state.neighborhood} type="text" name="neighborhood" placeholder={placeholderNeighborhood} required />
                            </Col>
                            <Col>
                                <Label for="">
                                    <Tr content="clientForm.stratum"/>
                                </Label>
                                <Input onChange={this.handleInput} value={this.state.stratus} type="number" name="stratus" placeholder={placeholderStratum} required />
                            </Col>
                        </Row>

                        <Label for="">
                            <Tr content="clientForm.phone"/>
                        </Label>
                        <Input onChange={this.handleInput} value={this.state.phone} type="number" name="phone" placeholder={placeholderPhone} required />
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

export default connect(mapStateToProps, mapDispatchToProps)(CreateUserForm);