import React from "react";
import CreateClientForm from "views/operator/CreateClientForm.jsx";
import axios from 'axios';


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
            persons: [],
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

    editUser = state => {
        // alert('Axios');
        // axios.post("https://energycorp.herokuapp.com/api/user/client/" + state.id + "/update/", state)
        //     .then(res => {
        //         alert("AXION REALIZADA CON EXITO");
        //     })
        //     .catch(err => {
        //         console.log(err);
        //     })
        this.closeToggle();
    }

    async componentDidMount() {
        const res = await fetch('https://energycorp.herokuapp.com/api/user/client/');

        const data = await res.json();

        this.setState({ persons: data });
    }

    render() {

        var filteredPeople = [];

        filteredPeople = this.state.persons.filter(p => (
            p.user.email.toLowerCase().indexOf(this.state.search.toLowerCase()) !== -1
        ));

        const people = filteredPeople.map((p, k) => (
            <tr key={k}>
                <th scope="row">#{k + 1}</th>
                <th>{p.user.id_user}</th>
                <th>{p.user.name}</th>
                <th>{p.user.phone}</th>
                <th>{p.user.email}</th>
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
                                                <th>ID</th>
                                                <th>Name</th>
                                                <th>Phone</th>
                                                <th>Email</th>
                                                <th>Review</th>
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
                                <CreateClientForm submitAction={this.editUser} user={this.state.user} editMode={true} />
                            </ModalBody>
                        </Modal>
                    </div>

                </Row>
            </div>
        )
    }
};

export default GetClients;