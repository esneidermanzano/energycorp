import React from "react";
import { Route, Redirect } from "react-router-dom";
import auth from "components/auth/auth.js";

export const ProtectedRoute = ({ render: Component, userType, ...rest }) => {
    return (
        <Route {...rest} render={props => {
            if (auth.isAuthenticated()) {

                if (auth.getType() === userType) {
                    return <Component {...props} />;
                } else {
                    return <Redirect to={{ pathname: "/" + auth.getType(), state: { from: props.location } }} />
                }

            } else {
                return <Redirect to={{ pathname: "/login", state: { from: props.location } }} />
            }
        }} />
    );
};

export const ProtectedLoginRoute = ({ component: Component, ...rest }) => {
    return (
        <Route {...rest} render={props => {
            if (auth.isAuthenticated()) {
                return <Redirect to={{ pathname: "/" + auth.getType(), state: { from: props.location } }} />
            } else {
                return <Component {...props} />;
            }
        }} />
    );
};