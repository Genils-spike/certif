import React from 'react';
import {Text, TouchableOpacity, TextInput, StyleSheet, View } from 'react-native';

export default class Signin extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        username : '',
        password : '',
        email: ''
      }
    }
    handleSubmit = () => {
      const { navigate } = this.props.navigation;
      console.log(this.state);
      fetch('http://192.168.0.31:8888/user/signup', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.state)
      })
      .then( (res) => { return res.json() } )
      .then( (data) => { 
        console.log(data);
      })
      .then ( () => navigate('Index'))
      .catch( err => { 
        console.log(err);
      });
    }

  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>
          Créer un compte
        </Text>
        <Text style={styles.text}>
          Nom d'utilisateur
        </Text>
        <TextInput style={styles.textinput}
          editable={true} 
          onChangeText={(username) => this.setState({username})}
          placeholder = 'Enter your login here'
          underlineColorAndroid='transparent'
        />
        <Text style={styles.text}>
          Email
        </Text>
        <TextInput style={styles.textinput}
          editable={true} 
          onChangeText={(email) => this.setState({email})}
          placeholder = 'Enter your Email here'
          underlineColorAndroid='transparent'
        />
        <Text style={styles.text}>
          Password
        </Text>
        <TextInput style={styles.textinput}
          editable={true} 
          onChangeText={(password) => this.setState({password})}
          placeholder = 'Enter your password here'
          underlineColorAndroid='transparent'
          secureTextEntry
        />
         <TouchableOpacity style= {styles.connexion}
          onPress={this.handleSubmit.bind(this)}
        >
          <Text style= {styles.textConnexion}>
            INSCRIPTION
          </Text>
        </TouchableOpacity>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#202020',
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    color:'#A1F700',  
    fontWeight: 'bold',
    fontSize: 25,
    paddingBottom: 15

  },
  text : {
    color: 'white',
    fontWeight: '100',
    fontSize: 12,
    marginBottom: 1
  },
  textinput: {
    backgroundColor: '#ffffff',
    borderColor: '#A1F700',
    borderWidth: 1,
    width: 250,
    height: 40,
    marginBottom: 8,
    paddingLeft: 5
  },
  connexion: {
    borderColor: '#A1F700',
    backgroundColor: '#A1F700',
    alignItems: 'center',
    borderWidth: 1,
    width:250,
    marginTop: 12
  },
  textConnexion:{
    fontSize: 20,
    letterSpacing: 7,
    color:'#202020',
    padding: 5
  },
  forgotPWD:{
    marginTop: 7,
    color: '#A1F700'
  }
});
