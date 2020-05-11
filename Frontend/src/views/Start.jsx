import React from "react";
import DemoNavbar from "components/Navbars/DemoNavbar.jsx";
import ChatBot from "components/chatBot/ChatBot.jsx";

import { Link } from "react-router-dom";

import counterpart from "counterpart";
import * as Tr from "react-translate-component";
import spanish from "../langs/spanish.js";
import english from "../langs/english.js";

import bot_gif from "./bot_gif.gif";

import { connect } from "react-redux";

// counterpart.registerTranslations('en', english);
// counterpart.registerTranslations('es', spanish);

 
// counterpart.setLocale('en');

class Start extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            visibleChat: false
        }
    }

    openChat = () => {
        this.setState({ visibleChat: true });
    }

    closeChat = () => {
        this.setState({ visibleChat: false });
    }

    render() {
        return (
            <div>
                <DemoNavbar {...this.props} />
                <div className="contentStart">
                    <center>
                        <Tr content="home.title" component="h1" />
                        <img width="744" height="490" src="https://www.mercapava.com.co/wp-content/uploads/2016/10/Tip-5.jpg" alt="description"></img>
                        <br></br>
                        <br></br>
                    </center>
                </div>
                {
                    this.state.visibleChat
                        ? <ChatBot close={this.closeChat} />
                        : <img onClick={this.openChat} className="floatingBot animated wobble" src={bot_gif} width="95px" height="120px" alt="description"></img>
                }

                <center>
                    <br />
                    <Link className="btn btn-danger" to="/getBill">
                        <Tr content="home.download" component="div" />
                    </Link>
                </center>
            </div>
        )
    }
}

const mapStateToProps = state => {
    counterpart.setLocale(state.language);
    return { lng: state.language }
}

const mapDispatchToProps = dispatch => ({});

export default connect(mapStateToProps, mapDispatchToProps)(Start);