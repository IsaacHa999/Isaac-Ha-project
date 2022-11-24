import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:sscc_talk/setting_page.dart';

class NoticePage extends StatefulWidget {
  const NoticePage({super.key});

  @override
  State<NoticePage> createState() => _NoticePageState();
}

class _NoticePageState extends State<NoticePage> {
  //좋아요 여부
  bool isFavorite = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        // appBar: AppBar(
        //   title: Text(
        //     '공지사항',
        //     style: TextStyle(
        //       color: Colors.black,
        //     ),
        //   ),
        //   centerTitle: true,
        //   elevation: 0,
        //   backgroundColor: Colors.white,
        //   actions: [
        //     IconButton(
        //       icon: Icon(Icons.settings),
        //       color: Colors.black,
        //       onPressed: (() {
        //         Navigator.push(
        //           context,
        //           MaterialPageRoute(builder: (_) => SettingPage()),
        //         );
        //       }),
        //     ),
        //   ],
        // ),
        body: Padding(
      padding: const EdgeInsets.all(25.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          //피드
          // Image.network(
          //   "https://i.ibb.co/CwzHq4z/trans-logo-512.png",
          //   height: 100,
          //   width: 100,
          //   fit: BoxFit.cover,
          // ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(
              "제목",
              style: TextStyle(
                fontWeight: FontWeight.bold,
              ),
            ),
          ),

          // 설명
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(
              "My cat is docile even when bathed. I put a duck on his head in the wick and he's staring at me. Isn't it so cute??",
            ),
          ),

          // 날짜
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(
              "FEBURARY 6",
              style: TextStyle(
                color: Colors.grey,
              ),
            ),
          ),
          Row(
            children: [
              IconButton(
                icon: Icon(
                  CupertinoIcons.heart,
                  color: isFavorite ? Colors.pink : Colors.black,
                ),
                onPressed: () {
                  setState(() {
                    //build가 다시 호출된다.
                    isFavorite = !isFavorite;
                  });
                },
              ),
              IconButton(
                icon: Icon(CupertinoIcons.chat_bubble, color: Colors.black),
                onPressed: () {},
              ),
              Spacer(),
              IconButton(
                icon: Icon(CupertinoIcons.bookmark, color: Colors.black),
                onPressed: () {},
              ),
            ],
          ),
          Divider()
        ],
      ),
    ));
  }
}



---------------------------------------------
      body: ListView.builder(
        itemCount: 10,
        itemBuilder: (context, index) {
          return Feed();
        },
      ),


      ---------------------
floatingActionButton: FloatingActionButton(
  onPressed: () {
    print("클릭 되었습니다!");
  },
  child: const Icon(
    Icons.add, #"+"아이콘
    color: Colors.amber,
  ),
  backgroundColor: Colors.white,
),