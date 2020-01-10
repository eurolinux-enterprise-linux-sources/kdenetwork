/*
 * Jingle call example
 * Copyright 2004--2005, Google Inc.
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */

// LinphoneMediaEngine is a Linphone implementation of MediaEngine

#ifndef TALK_SESSION_PHONE_LINPHONEMEDIAENGINE_H_
#define TALK_SESSION_PHONE_LINPHONEMEDIAENGINE_H_

extern "C" {
#include <mediastreamer2/mediastream.h>
}
#include "talk/base/asyncsocket.h"
#include "talk/base/scoped_ptr.h"
#include "talk/session/phone/mediaengine.h"

namespace cricket {

class LinphoneMediaEngine;

class LinphoneMediaChannel : public MediaChannel {
 public:
  LinphoneMediaChannel(LinphoneMediaEngine *eng);
  virtual ~LinphoneMediaChannel();

  virtual void SetCodecs(const std::vector<Codec> &codecs);
  virtual void OnPacketReceived(const void *data, int len);
  virtual void StartRing(bool bIncomingCall);
  virtual void StopRing();

  virtual void SetPlayout(bool playout);
  virtual void SetSend(bool send);


  virtual int GetOutputLevel();
  bool mute() {return mute_;}

  virtual void StartMediaMonitor(VoiceChannel * voice_channel, uint32 cms) {}
  virtual void StopMediaMonitor() {}
   
 private:
  RingStream* ring_stream_;
  LinphoneMediaEngine *engine_;
  AudioStream *audio_stream_;
  talk_base::scoped_ptr<talk_base::AsyncSocket> socket_;
  void OnIncomingData(talk_base::AsyncSocket *s);
  int pt_;
  bool mute_;
  bool play_;
  int port1; // local port for audio_stream
  int port2; // local port for rtp
};

class LinphoneMediaEngine : public MediaEngine {
 public:
  LinphoneMediaEngine(const std::string& ringWav,  const std::string& callWav);
  ~LinphoneMediaEngine();
  virtual bool Init() {return true;}
  virtual void Terminate();
  
  virtual MediaChannel *CreateChannel();

  virtual int SetAudioOptions(int options);
  virtual int SetSoundDevices(int wave_in_device, int wave_out_device);

  virtual float GetCurrentQuality();
  virtual int GetInputLevel();
  
  virtual std::vector<Codec, std::allocator<Codec> > codecs() {return codecs_;}
  virtual bool FindCodec(const Codec&);

  std::string GetRingWav(){return ring_wav_;}
  std::string GetCallWav(){return call_wav_;}

  bool have_ilbc;
  bool have_speex;
  bool have_gsm;

 private:
  std::vector<Codec, std::allocator<Codec> > codecs_;

  std::string ring_wav_;
  std::string call_wav_;
};

}  // namespace cricket

#endif  // TALK_SESSION_PHONE_LINPHONEMEDIAENGINE_H_
