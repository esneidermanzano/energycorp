import React from "react";
import CreateUserForm from "views/admin/CreateUserForm.jsx";

import {
    Card,
    CardBody,
    Row,
    Col, FormGroup, Input, Button, Table,
    Modal, ModalHeader, ModalBody
} from "reactstrap";

class GetUser extends React.Component {
    constructor(props) {
        super(props);
        this.state = { //PHONE IS NUMBER
            persons: [
                {
                    ID: 121,
                    name: 'charles',
                    lastname: 'pirlo',
                    email: 'murillo.carlos@correounivalle.edu.co',
                    adress: 'sdsds',
                    phone: 3001234567,
                    sex: 'Male',
                    date: '2020-02-26',
                    type: 'Cliente',
                    client: {
                        typeCli: 'Natural',
                        tasa_interes_Mora: 2.0,
                        ciclo: 1,
                        contrato: '1001',
                        facturacion: '3343442',
                        estado_financiero: 'Mora',
                        ID_contador: '100021',
                    }
                },
                {
                    ID: 232,
                    name: 'Aida',
                    lastname: 'Merlano',
                    email: 'messi.carlos@correounivalle.edu.co',
                    adress: 'sdsds',
                    phone: 3001234567,
                    sex: 'Female',
                    date: '2020-02-26',
                    type: 'Operador',
                    client: {}
                },
                {
                    ID: 233,
                    name: 'James',
                    lastname: 'Rodriguez',
                    email: 'james.carlos@correounivalle.edu.co',
                    adress: 'sdsds',
                    phone: 3001234567,
                    sex: 'Female',
                    date: '2020-02-26',
                    type: 'Operador',
                    client: {}
                },
                {
                    ID: 344,
                    name: 'Trevor',
                    lastname: 'Philips',
                    email: 'ronaldo@cristiano.com',
                    adress: 'sdsds',
                    phone: 3001234567,
                    sex: 'Male',
                    date: '2020-02-26',
                    type: 'Gerente',
                    client: {}
                },
                {
                    ID: 345,
                    name: 'Duvan',
                    lastname: 'vergara',
                    email: 'zlatan@correounivalle.edu.co',
                    adress: 'sdsds',
                    phone: 3001234567,
                    sex: 'Female',
                    date: '2020-02-26',
                    type: 'Operador',
                    client: {}
                },
                {
                    ID: 346,
                    name: 'Reinaldo',
                    lastname: 'Rueda',
                    email: 'rodallega@correounivalle.edu.co',
                    adress: 'sdsds',
                    phone: 3001234567,
                    sex: 'Female',
                    date: '2020-02-26',
                    type: 'Operador',
                    client: {}
                },
                {
                    ID: 347,
                    name: 'charles',
                    lastname: 'Perez',
                    email: 'maradona@gmail.com',
                    adress: 'sdsds',
                    phone: 3001234567,
                    sex: 'Male',
                    date: '2020-02-26',
                    type: 'Gerente',
                    client: {}
                },
                {
                    ID: 457,
                    name: 'Mariana',
                    lastname: 'Pajon',
                    email: 'modric@gmail.com',
                    adress: 'sdsds',
                    phone: 3001234567,
                    sex: 'Male',
                    date: '2020-02-26',
                    type: 'Operador',
                    client: {}
                },
                {
                    ID: 458,
                    name: 'Quentin',
                    lastname: 'Tarantino',
                    email: 'suarez@gmail.com',
                    adress: 'sdsds',
                    phone: 3001234567,
                    sex: 'Male',
                    date: '2020-02-26',
                    type: 'Gerente',
                    client: {}
                },
                {
                    ID: 569,
                    name: 'Bong',
                    lastname: 'Jonh Jo',
                    email: 'parasite@gmail.com',
                    adress: 'sdsds',
                    phone: 3001234567,
                    sex: 'Male',
                    date: '2020-02-26',
                    type: 'Cliente',
                    client: {
                        typeCli: 'Juridica',
                        tasa_interes_Mora: 2.0,
                        ciclo: 1,
                        contrato: '1001',
                        facturacion: '3343442',
                        estado_financiero: 'Mora',
                        ID_contador: '330021',
                    }
                },
            ],
            search: '',
            modal: false,
            selected: 'All',
            user: {},
        }
    }

    handleInput = e => {
        this.setState({
            [e.target.name]: e.target.value
        });
    }

    openToggle = obj => {
        this.setState({
            user: obj,
            modal: true
        });
    }

    closeToggle = () => {
        this.setState({
            modal: false
        });
    }

    editUser = () => {
        alert('Axios');
        this.closeToggle();
    }

    render() {

        var filteredPeople = [];

        if (this.state.selected !== 'All') { //Filtrar por ambas formas al tiempo
            filteredPeople = this.state.persons.filter(p => (
                p.type.toLowerCase() === this.state.selected.toLowerCase() &&
                p.email.toLowerCase().indexOf(this.state.search.toLowerCase()) !== -1
            ));
        }else{ //Filtrar solo por busqueda
            filteredPeople = this.state.persons.filter(p => (
                p.email.toLowerCase().indexOf(this.state.search.toLowerCase()) !== -1
            ));
        }

        const people = filteredPeople.map((p, k) => (
            <tr key={k}>
                <th scope="row">#{k + 1}</th>
                <th>{p.name}</th>
                <th>{p.lastname}</th>
                <th>{p.ID}</th>
                <th>{p.email}</th>
                <th>{p.type}</th>
                <th>
                    <Button color="success" onClick={() => this.openToggle(p)}>
                        <i className="nc-icon nc-zoom-split" />
                    </Button>
                </th>
            </tr>
        ));

        return (
            <div className="content">
                <Row>
                    <Col sm="12">
                        <br></br>
                        <Card >
                            <CardBody>
                                <Col>
                                    <Row>
                                        <Col>
                                            <select onChange={this.handleInput} className="form-control" name="selected">
                                                <option>All</option>
                                                <option>Operador</option>
                                                <option>Gerente</option>
                                                <option>Cliente</option>
                                            </select>
                                        </Col>
                                        <Col>
                                            <FormGroup>
                                                <Input onChange={this.handleInput} name="search" placeholder="Search"></Input>
                                            </FormGroup>
                                        </Col>
                                    </Row>
                                    <br></br>
                                    <Table responsive>
                                        <thead>
                                            <tr>
                                                <th>#</th>
                                                <th>First Name</th>
                                                <th>Last Name</th>
                                                <th>ID</th>
                                                <th>Email</th>
                                                <th>Type</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {people}
                                        </tbody>
                                    </Table>
                                </Col>
                            </CardBody>
                        </Card>
                    </Col>

                    <div>
                        <Modal md="7" isOpen={this.state.modal} toggle={this.closeToggle} className="danger">
                            <ModalHeader toggle={this.closeToggle}>Edit User</ModalHeader>
                            <ModalBody>
                                <CreateUserForm submitAction={this.editUser} user={this.state.user} />
                            </ModalBody>
                        </Modal>
                    </div>

                </Row>
            </div>
        )
    }
};

export default GetUser;