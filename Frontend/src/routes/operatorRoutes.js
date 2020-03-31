import CreateClient from "views/operator/CreateClient.jsx";
import GetClients from "views/operator/GetClients.jsx";

var operatorRoutes = [
  {
    path: "/createClient",
    name: "createClient",
    icon: "nc-icon nc-diamond",
    component: CreateClient,
    layout: "/operator"
  },
  {
    path: "/getClients",
    name: "getClients",
    icon: "nc-icon nc-pin-3",
    component: GetClients,
    layout: "/operator"
  }
];

export default operatorRoutes;
