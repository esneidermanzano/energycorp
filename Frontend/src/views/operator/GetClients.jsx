import React from "react";
import CreateClientForm from "views/operator/CreateClientForm.jsx";

import {
    Card,
    CardBody,
    Row,
    Col, FormGroup, Input, Button, Table,
    Modal, ModalHeader, ModalBody
} from "reactstrap";

class GetClients extends React.Component {
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
                    phone: 'dfdfdfd',
                    sex: 'Male',
                    date: '2020-02-26'
                },
                {
                    ID: 232,
                    name: 'charles',
                    lastname: 'pirlo',
                    email: 'messi.carlos@correounivalle.edu.co',
                    adress: 'sdsds',
                    phone: 'dfdfdfd',
                    sex: 'Male',
                    date: '2020-02-26'
                },
                {
                    ID: 233,
                    name: 'werwe',
                    lastname: 'pirlo',
                    email: 'james.carlos@correounivalle.edu.co',
                    adress: 'sdsds',
                    phone: 'dfdfdfd',
                    sex: 'Female',
                    date: '2020-02-26'
                },
                {
                    ID: 344,
                    name: 'charles',
                    lastname: 'pirlo',
                    email: 'ronaldo@cristiano.com',
                    adress: 'sdsds',
                    phone: 'dfdfdfd',
                    sex: 'Male',
                    date: '2020-02-26'
                },
                {
                    ID: 345,
                    name: 'chaertertreterles',
                    lastname: 'pirlo',
                    email: 'zlatan@correounivalle.edu.co',
                    adress: 'sdsds',
                    phone: 'dfdfdfd',
                    sex: 'Female',
                    date: '2020-02-26'
                },
                {
                    ID: 346,
                    name: 'rtertete',
                    lastname: 'pirlo',
                    email: 'rodallega@correounivalle.edu.co',
                    adress: 'sdsds',
                    phone: 'dfdfdfd',
                    sex: 'Female',
                    date: '2020-02-26'
                },
                {
                    ID: 347,
                    name: 'charles',
                    lastname: 'pirlo',
                    email: 'maradona@gmail.com',
                    adress: 'sdsds',
                    phone: 'dfdfdfd',
                    sex: 'Male',
                    date: '2020-02-26'
                },
                {
                    ID: 457,
                    name: 'charles',
                    lastname: 'pirlo',
                    email: 'modric@gmail.com',
                    adress: 'sdsds',
                    phone: 'dfdfdfd',
                    sex: 'Male',
                    date: '2020-02-26'
                },
                {
                    ID: 458,
                    name: 'charles',
                    lastname: 'pirlo',
                    email: 'suarez@gmail.com',
                    adress: 'sdsds',
                    phone: 'dfdfdfd',
                    sex: 'Male',
                    date: '2020-02-26'
                },
                {
                    ID: 569,
                    name: 'charles',
                    lastname: 'pirlo',
                    email: 'parasite@gmail.com',
                    adress: 'sdsds',
                    phone: 'dfdfdfd',
                    sex: 'Male',
                    date: '2020-02-26'
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

        filteredPeople = this.state.persons.filter(p => (
            p.email.toLowerCase().indexOf(this.state.search.toLowerCase()) !== -1
        ));

        const people = filteredPeople.map((p, k) => (
            <tr key={k}>
                <th scope="row">#{k + 1}</th>
                <th>{p.name}</th>
                <th>{p.lastname}</th>
                <th>{p.ID}</th>
                <th>{p.email}</th>
                <th>
                    <Button color="warning" onClick={() => this.openToggle(p)}>
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
                                        <FormGroup>
                                            <Input onChange={this.handleInput} name="search" placeholder="Search"></Input>
                                        </FormGroup>
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
                                <CreateClientForm submitAction={this.editUser} user={this.state.user} />
                            </ModalBody>
                        </Modal>
                    </div>

                </Row>
            </div>
        )
    }
};

export default GetClients;