# Discord-Friend-Link-Generator
This is a Friend Link Generator written in python for discord. It uses discord's latest api (currently v9) to get a friend link code.  
These are very similar to the server invite links and look like this when you send them in Discord: 
![image](https://github.com/whois-hoeless/Discord-Friend-Link-Generator/assets/85312115/a0ed781f-9a41-4499-b4a9-ff8005047818)


So far I have not found a way to change the default max_age and max_uses which set the amount of time the link will be working and the amount of people being able to use it.

`max_age` = 604800 (seconds) = 1 week  
`max_uses` = 5 (5 people can use the link)  

If you don't want to find your token to use this then you can also just paste some js code inside the console of your current discord session:
```js
webpackChunkdiscord_app.push([[[Math.random()]],{},q=>Object.values(q.c).find(e=>e.exports?.Z?.createFriendInvite).exports.Z.createFriendInvite().then(x => console.log('discord.gg/' + x.code))])
```

### Warining
**THIS IS AGAINST DISCORDS TOS**  
Yet I believe the chance of getting banned for this is very low..



Credits goes to [this gist](https://gist.github.com/oSumAtrIX/8c0540c80ca2b91efa18d137e239570f) aswell, its the reason I wrote this.
