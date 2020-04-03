import React from "react";

// reactstrap components
import {
    Row, Col, Form, FormGroup, Label, Input, Button
} from "reactstrap";

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

        const addBtn = (!this.props.user) ? <Button color="warning">Add</Button> : <Button color="warning">Edit</Button>;

        const showStateAttr = this.props.editMode ? <div> <Label for="">Estado</Label>
            <select onChange={this.handleInput} value={this.state.user.is_active} className="form-control" name="is_active" required>
                <option>Activo</option>
                <option>Inactivo</option>
            </select>
        </div> : true


        const aditional =
            <div>
                <center style={{ marginTop: "2em" }}>Aditional Information</center>

                <Row>
                    <Col>
                        <Label for="">Tipo</Label>
                        <select onChange={this.handleInputClient} value={this.state.type_client} className="form-control" name="type_client" required>
                            <option value="1">Natural</option>
                            <option value="2">Juridica</option>
                        </select>
                    </Col>
                    <Col>
                        <Label for="">Tasa Interes mora</Label>
                        <Input onChange={this.handleInputClient} value={this.state.interes_mora} type="number" step="0.01" name="interes_mora" placeholder="Tasa Interes mora" required />
                    </Col>
                </Row>

                <Row>
                    <Col>
                        <Label for="">Ciclo</Label>
                        <Input onChange={this.handleInputClient} value={this.state.cycle} type="number" name="cycle" placeholder="ciclo" required />
                    </Col>
                    <Col>
                        <Label for="">Numero de contrato</Label>
                        <Input onChange={this.handleInputClient} value={this.state.contrat_number} type="text" name="contrat_number" placeholder="contrato" required />
                    </Col>
                </Row>

                <Row>
                    <Col>
                        <Label for="">Facturacion</Label>
                        <Input onChange={this.handleInputClient} value={this.state.billing} type="number" name="billing" placeholder="facturacion" required />
                    </Col>
                    <Col>
                        <Label for="">Estado Financiero</Label>
                        <select onChange={this.handleInputClient} value={this.state.financial_state} className="form-control" name="financial_state" required>
                            <option value="Mora">Mora</option>
                            <option value="No Mora">No Mora</option>
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
                                <Label for="">Nombre</Label>
                                <Input onChange={this.handleInput} value={this.state.user.name} type="text" name="name" placeholder="Nombre" required />
                            </Col>
                        </Row>
                        <Label for="">Email</Label>
                        <Input onChange={this.handleInput} value={this.state.user.email} type="email" name="email" placeholder="Email" required />

                        <Row>
                            <Col>
                                <Label for="">Direccion</Label>
                                <Input onChange={this.handleInput} value={this.state.user.address} type="text" name="address" placeholder="Direccion" required />
                            </Col>
                            <Col>
                                <Label for="">Barrio</Label>
                                <Input onChange={this.handleInput} value={this.state.user.neighborhood} type="text" name="neighborhood" placeholder="Barrio" required />
                            </Col>
                            <Col>
                                <Label for="">Estrato</Label>
                                <Input onChange={this.handleInput} value={this.state.user.stratus} type="number" name="stratus" placeholder="Estrato" required />
                            </Col>
                        </Row>

                        <Label for="">Telefono</Label>
                        <Input onChange={this.handleInput} value={this.state.user.phone} type="number" name="phone" placeholder="Telefono" required />
                        {showStateAttr}
                        {aditional}
                    </div>
                </FormGroup>
                {addBtn}
            </Form>
        )
    }
};

export default CreateClientForm;