import React from 'react';
import {  StackNavigator } from 'react-navigation';
import Login from "./layouts/login";
import Index from "./layouts/index";
import Signin from "./layouts/signin";

export const Navigation = StackNavigator({
	Index: { screen: Index },
	Login: { screen: Login },
	Signin: { screen: Signin }
},
{ navigationOptions: {
header: null
}})