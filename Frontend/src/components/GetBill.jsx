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

import counterpart from "counterpart";
import * as Tr from "react-translate-component";
import spanish from "../langs/spanish.js";
import english from "../langs/english.js";
import portuguese from "../langs/portuguese.js";

import { connect } from "react-redux";

counterpart.registerTranslations('en', english);
counterpart.registerTranslations('es', spanish);
counterpart.registerTranslations('po', portuguese);

class Start extends React.Component {
    constructor(props) {
        super(props);
        this.state = {}
    }

    render() {

        const placeholderID = counterpart.translate('getBill.insert');

        return (
            <Col md="4" id="login">
                <Card>
                    <CardHeader>
                        <center>
                            <img src={logo} width="80px" height="80px" alt="description"></img>
                            <CardTitle tag="h5">
                                <Tr content="home.download"/>
                            </CardTitle>
                        </center>

                    </CardHeader>
                    <CardBody>
                        <Form>
                            <FormGroup>
                                <Label for="exampleEmail">ID</Label>
                                <Input type="number" name="id" id="exampleEmail" placeholder={placeholderID} />
                            </FormGroup>
                            <center>
                                <Button color="success">
                                    <Tr content="getBill.download"/>
                                </Button>
                                <br />
                                <Link to="/">
                                    <Tr content="getBill.home"/>
                                </Link>
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

const mapStateToProps = state => {
    counterpart.setLocale(state.language);
    return { lng: state.language }
}

const mapDispatchToProps = dispatch => ({});

export default connect(mapStateToProps, mapDispatchToProps)(Start);