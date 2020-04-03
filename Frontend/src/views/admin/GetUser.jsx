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

    editUser = () => {
        this.closeToggle();
    }

    parseToShow = user => {      
        let parsed = {
                user_type: '',
                id_user: user.user.id_user,
                name: user.user.name,
                email: user.user.email,
                address: user.user.address,
                neighborhood: user.user.neighborhood,
                phone: user.user.phone,
                is_active: user.user.is_active,
                client: {
                    type_client: user.type_client,
                    interes_mora: user.interes_mora,
                    cycle: user.cycle,
                    contrat_number: user.contrat_number,
                    billing: user.billing,
                    financial_state: user.financial_state,
                }            
        }

        if(user.usertype === 2){
            parsed.user_type = 'operador';
        }else{
            parsed.user_type = 'gerente';
        }
    
        return parsed;
    }

    render() {

        var filteredPeople = [];

        if (this.state.selected !== 'All') { //Filtrar por ambas formas al tiempo
            filteredPeople = this.state.persons.filter(p => (
                p.user_type.toLowerCase() === this.state.selected.toLowerCase() &&
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
                <th>{p.id_user}</th>
                <th>{p.email}</th>
                <th>{p.user_type}</th>
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
                                <CreateUserForm submitAction={this.editUser} user={this.state.user} editMode={true}/>
                            </ModalBody>
                        </Modal>
                    </div>

                </Row>
            </div>
        )
    }

    async componentDidMount() {
        const res = await fetch('https://energycorp.herokuapp.com/api/user/worker/');
        const data = await res.json();

        var parsedData = [];
        for(let i=0; i<data.length; i++){
            parsedData.push(this.parseToShow(data[i]));
        }

        this.setState({persons: parsedData});
    }

};

export default GetUser;

