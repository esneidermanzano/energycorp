import CreateUser from "views/admin/CreateUser.jsx";
import GetUser from "views/admin/GetUser.jsx";
import TransformersMap from "views/admin/TransformersMap.jsx";

var adminRoutes = [
  {
    path: "/createUser",
    name: "createUser",
    icon: "nc-icon nc-diamond",
    component: CreateUser,
    layout: "/admin"
  },
  {
    path: "/getUser",
    name: "getUser",
    icon: "nc-icon nc-pin-3",
    component: GetUser,
    layout: "/admin"
  },
  {
    path: "/transformersMap",
    name: "Map",
    icon: "nc-icon nc-pin-3",
    component: TransformersMap,
    layout: "/admin"
  }
];

export default adminRoutes;
