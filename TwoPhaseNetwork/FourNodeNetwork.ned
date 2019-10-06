//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
// 
// You should have received a copy of the GNU Lesser General Public License
// along with this program.  If not, see http://www.gnu.org/licenses/.
// 

package org.omnetpp.queueing;

//
// TODO auto-generated type
//
network FourNodeNetwork
{
    @display("bgb=380,205");
    submodules:
        Source: Source {
            @display("p=25,93");
        }
        //Router: Router {
          //  @display("p=117,93");
            //gates:
              //  out[2];
        //}
        PS: Server {
            @display("p=199,93");
        }
        SS1: Queue {
            @display("p=281,28");
        }
        SS2: Queue {
            @display("p=281,161");
        }
        //Classifier: Classifier {
        //    @display("p=343,93");
        //}
        sink: Sink {
            @display("p=343,93");
        }
        QueueU1: PassiveQueue {
            @display("p=117,28");
        }
        QueueU2: PassiveQueue {
            @display("p=117,161");
        }

    connections:
        //Source.out --> Router.in++;
        //Router.out[0] --> QueueU2.in++;
        //Router.out[1] --> QueueU1.in++;
        Source.out1 --> QueueU1.in++;
        Source.out2 --> QueueU2.in++;
        QueueU1.out++ --> PS.in++;
        QueueU2.out++ --> PS.in++;
        //PS.out --> Classifier.in++;
        PS.outU1 --> SS1.in++;
        PS.outU2 --> SS2.in++;
        PS.outSink --> sink.in++;
        SS1.out --> QueueU1.in++;
        SS2.out --> QueueU2.in++;
        //Classifier.rest --> sink.in++;
        //Classifier.out++ --> SS2.in++;
        //Classifier.out++ --> SS1.in++;

}
