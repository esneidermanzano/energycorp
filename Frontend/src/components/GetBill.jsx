import React from "react";

import logo from "logo.svg";

import { Link } from "react-router-dom";

import {
    Card,
    CardHeader,
    CardBody,
    CardFooter,
    CardTitle,
    Col, Form, FormGroup, Label, Input, Button
} from "reactstrap";

class Start extends React.Component {
    constructor(props) {
        super(props);
        this.state = {}
    }

    render() {
        return (
            <Col md="4" id="login">
                <Card>
                    <CardHeader>
                        <center>
                            <img src={logo} width="80px" height="80px" alt="description"></img>
                            <CardTitle tag="h5">Download your Bill</CardTitle>
                        </center>

                    </CardHeader>
                    <CardBody>
                        <Form>
                            <FormGroup>
                                <Label for="exampleEmail">ID</Label>
                                <Input type="number" name="id" id="exampleEmail" placeholder="Insert your ID" />
                            </FormGroup>
                            <center>
                                <Button color="success">download</Button>
                                <br />
                                <Link to="/">Home</Link>
                            </center>
                        </Form>
                    </CardBody>
                    <CardFooter>

                    </CardFooter>
                </Card>
            </Col>
        )
    }
}

export default Start;