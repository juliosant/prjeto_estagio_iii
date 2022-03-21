import 'package:flutter/material.dart';
import 'package:recycle_project/agendamento.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.lightGreen,
      ),
      home:  HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  //const HomePage({Key? key}) : super(key: key);

  Schedule scheduleService = Schedule();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Doações Agendadas"),
      ),
      body: Container(
        child: FutureBuilder<List>(
          future: scheduleService.getAllSchedule(),
          builder: (context, snapshot){
            print(snapshot.data);
            if(snapshot.hasData){
              return ListView.builder(
                  itemCount: snapshot.data?.length,
                  itemBuilder: (context, i){
                    return Card(
                      child: ListTile(
                        title: Text(snapshot.data![i]['dat_agendamento'],
                          style: TextStyle(
                            fontSize: 30.0,
                          ),
                        ),
                        subtitle: Text(
                            snapshot.data![i]['des_destinatario'],
                            style: TextStyle(
                              fontSize: 30.0,
                            )
                        ),
                      ),
                    );
                  }
              );
            }
            else{
              return const Center(
                child: Text('Sem dados'),
              );
            }
          }
        ),
      ),





    );
  }
}


