import React from 'react';
import { AsyncStorage, Text, TouchableOpacity, TextInput, StyleSheet, View } from 'react-native';

export default class Login extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        login : '',
        password : ''
      }
    }
        handleSubmit = () => {
      const { navigate } = this.props.navigation;
      fetch('http://192.168.0.31:8888/user/login', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.state)
      })
      .then( (res) => { return res.json() } )
      .then( (data) => { 
        try {
          AsyncStorage.setItem('user_id', data.user_id);
        }
        catch (error) {
          console.log(error)
        }
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
          Connexion
        </Text>
        <Text style={styles.text}>
          Nom d'utilisateur
        </Text>
        <TextInput style={styles.textinput}
          editable={true} 
          onChangeText={(login) => this.setState({login})}
          placeholder = 'Enter your login here'
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
            Connexion
          </Text>
        </TouchableOpacity>
        <TouchableOpacity>
          <Text style={styles.forgotPWD}>
            Identifiants oubliés?
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
