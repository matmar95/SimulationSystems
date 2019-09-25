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
    @display("bgb=501,312");
    submodules:
        Source: Source {
            @display("p=44,167");
        }
        PS: Server {
            @display("p=194,167");
        }
        SS1: Queue {
            @display("p=331,97");
        }
        SS2: Queue {
            @display("p=331,243");
        }
        Classifier: Classifier {
            @display("p=331,167");
        }
        sink: Sink {
            @display("p=432,167");
        }
        Queue: PassiveQueue {
            @display("p=122,167");
        }
    connections:
        Source.out --> Queue.in++;
        PS.out --> Classifier.in++;
        SS1.out --> Queue.in++;
        SS2.out --> Queue.in++;
        Queue.out++ --> PS.in++;
        Classifier.rest --> sink.in++;
        Classifier.out++ --> SS2.in++;
        Classifier.out++ --> SS1.in++;

}
