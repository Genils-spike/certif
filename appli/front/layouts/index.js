import React from 'react';
import {AsyncStorage,Text, TouchableOpacity, StyleSheet, View } from 'react-native';


export default class Index extends React.Component {
  componentDidMount: function() {
        AsyncStorage.getItem("user_id").then((value) => {
            this.setState({"user_id": value});
        }).done();
    },

  render() {
    const { navigate } = this.props.navigation;
    return (
      
  console.log({this.state.myKey});
      <View style={styles.container}>
        <Text style={styles.title}>
          RENZEN
        </Text>
        <TouchableOpacity style= {styles.connexion}
          onPress={() => navigate('Login')}
        >
          <Text style= {styles.textConnexion}>
            Connexion
          </Text>
        </TouchableOpacity>
        <TouchableOpacity style= {styles.inscription}
          onPress={() => navigate('Signin')}
        >
          <Text style= {styles.textInscription}>
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
    color:'white',  
    fontWeight: '600',
    fontSize: 40,
    paddingBottom: 15

  },
  connexion: {
    borderColor: '#A1F700',
    alignItems: 'center',
    borderWidth: 1,
    width:250,
    marginBottom: 15
  },
  inscription: {
    borderColor: '#A1F700',
    backgroundColor: '#A1F700',
    alignItems: 'center',
    borderWidth: 1,
    width:250
  },
  textConnexion: {
    fontSize: 20,
    letterSpacing: 7,
    color:'#A1F700',
    padding: 5
  },
  textInscription:{
    fontSize: 20,
    letterSpacing: 7,
    color:'#202020',
    padding: 5
  }
})