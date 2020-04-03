import React from "react";

// reactstrap components
import {
    Row, Col, Form, FormGroup, Label, Input, Button
} from "reactstrap";

class CreateUserForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = this.props.user || {
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
        }

        if (e.target.name === "stratus") {
            val = parseInt(val);
        }

        if (e.target.name === "user_type") {
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

        const addBtn = (!this.props.user) ? <Button color="success">Add</Button> : <Button color="success">Edit</Button>;

        const showStateAttr = this.props.editMode ? <div> <Label for="">Estado</Label>
            <select onChange={this.handleInput} value={this.state.is_active} className="form-control" name="is_active" required>
                <option>Activo</option>
                <option>Inactivo</option>
            </select>
        </div> : true

        const aditional = (this.state.user_type === 'Cliente') ? <div>
            <center style={{ marginTop: "2em" }}>Aditional Information</center>

            <Row>
                <Col>
                    <Label for="">Tipo</Label>
                    <select onChange={this.handleInputClient} value={this.state.client.type_client} className="form-control" name="type_client" required>
                        <option>Natural</option>
                        <option>Juridica</option>
                    </select>
                </Col>
                <Col>
                    <Label for="">Tasa Interes mora</Label>
                    <Input onChange={this.handleInputClient} value={this.state.client.interes_mora} type="number" name="interes_mora" placeholder="Tasa Interes mora" required />
                </Col>
            </Row>

            <Row>
                <Col>
                    <Label for="">Ciclo</Label>
                    <Input onChange={this.handleInputClient} value={this.state.client.cycle} type="number" name="cycle" placeholder="ciclo" required />
                </Col>
                <Col>
                    <Label for="">Numero de contrato</Label>
                    <Input onChange={this.handleInputClient} value={this.state.client.contrat_number} type="text" name="contrat_number" placeholder="contrato" required />
                </Col>
            </Row>

            <Row>
                <Col>
                    <Label for="">Facturacion</Label>
                    <Input onChange={this.handleInputClient} value={this.state.client.billing} type="number" name="billing" placeholder="facturacion" required />
                </Col>
                <Col>
                    <Label for="">Estado Financiero</Label>
                    <select onChange={this.handleInputClient} value={this.state.client.financial_state} className="form-control" name="financial_state" required>
                        <option>Mora</option>
                        <option>No Mora</option>
                    </select>
                </Col>
            </Row>

        </div> : true

        return (
            <Form id="form" onSubmit={this.handleSubmit}>
                <FormGroup>
                    <div>
                        <Label for="">Tipo de usuario</Label>
                        <select onChange={this.handleInput} value={this.state.user_type} className="form-control" name="user_type" required>
                            <option value = "2">Operador</option>
                            <option value = "3">Gerente</option>
                        </select>
                        <Row>
                            <Col>
                                <Label for="">ID</Label>
                                <Input onChange={this.handleInput} value={this.state.id_user} type="number" name="id_user" placeholder="ID" required />
                            </Col>
                        </Row>

                        <Row>
                            <Col>
                                <Label for="">Nombre</Label>
                                <Input onChange={this.handleInput} value={this.state.name} type="text" name="name" placeholder="Nombre" required />
                            </Col>
                        </Row>
                        <Label for="">Email</Label>
                        <Input onChange={this.handleInput} value={this.state.email} type="email" name="email" placeholder="Email" required />

                        <Row>
                            <Col>
                                <Label for="">Direccion</Label>
                                <Input onChange={this.handleInput} value={this.state.address} type="text" name="address" placeholder="Direccion" required />
                            </Col>
                            <Col>
                                <Label for="">Barrio</Label>
                                <Input onChange={this.handleInput} value={this.state.neighborhood} type="text" name="neighborhood" placeholder="Barrio" required />
                            </Col>
                            <Col>
                                <Label for="">Estrato</Label>
                                <Input onChange={this.handleInput} value={this.state.stratus} type="number" name="stratus" placeholder="Estrato" required />
                            </Col>
                        </Row>

                        <Label for="">Telefono</Label>
                        <Input onChange={this.handleInput} value={this.state.phone} type="number" name="phone" placeholder="Telefono" required />
                        {showStateAttr}
                        {aditional}
                    </div>
                </FormGroup>
                {addBtn}
            </Form>
        )
    }
};

export default CreateUserForm;