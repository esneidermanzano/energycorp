import React from "react";

// reactstrap components
import {
    Row, Col, Form, FormGroup, Label, Input, Button
} from "reactstrap";

class CreateClientForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = this.props.user || {
            ID: '',
            sex: '',
            name: '',
            lastname: '',
            email: '',
            adress: '',
            phone: '',
            date: ''
        }
    }

    handleInput = e => {
        this.setState({
            [e.target.name]: e.target.value
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
            ID: '',
            sex: '',
            name: '',
            lastname: '',
            email: '',
            adress: '',
            phone: '',
            date: ''
        });
    }

    render() {

        const addBtn = (!this.props.user) ? <Button color="warning">Add</Button> : <Button color="warning">Edit</Button>;

        return (
            <Form id="form" onSubmit={this.handleSubmit}>
                <FormGroup>
                    <Row>
                        <Col>
                            <Label for="">ID</Label>
                            <Input onChange={this.handleInput} value={this.state.ID} type="number" name="ID" placeholder="ID" required />
                        </Col>
                        <Col>
                            <Label for="">Sex</Label>
                            <select onChange={this.handleInput} value={this.state.sex} className="form-control" name="sex" required>
                                <option>Female</option>
                                <option>Male</option>
                            </select>
                        </Col>
                    </Row>

                    <Label for="">Nombre</Label>
                    <Input onChange={this.handleInput} value={this.state.name} type="text" name="name" placeholder="Nombre" required />
                    <Label for="">Apellido</Label>
                    <Input onChange={this.handleInput} value={this.state.lastname} type="text" name="lastname" placeholder="Apellido" required />
                    <Label for="">Email</Label>
                    <Input onChange={this.handleInput} value={this.state.email} type="email" name="email" placeholder="Email" required />
                    <Label for="">Direccion</Label>
                    <Input onChange={this.handleInput} value={this.state.adress} type="text" name="adress" placeholder="Direccion" required />
                    <Label for="">Telefono</Label>
                    <Input onChange={this.handleInput} value={this.state.phone} type="number" name="phone" placeholder="Telefono" required />
                    <Label for="">Fecha de Nacimiento</Label>
                    <Input onChange={this.handleInput} value={this.state.date} type="date" name="date" placeholder="Fecha" required />

                </FormGroup>
                {addBtn}
            </Form>
        )
    }
};

export default CreateClientForm;