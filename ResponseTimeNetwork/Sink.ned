//
// This file is part of an OMNeT++/OMNEST simulation example.
//
// Copyright (C) 2006-2015 OpenSim Ltd.
//
// This file is distributed WITHOUT ANY WARRANTY. See the file
// `license' for details on this and other legal matters.
//

package org.omnetpp.queueing;

//
// Destroys (or optionally keep) the packets and collects statistics
//
simple Sink
{
    parameters:
        @group(Queueing);
        @display("i=block/sink");
        @signal[lifeTime](type="simtime_t");
        @signal[lifeTimeU1](type="simtime_t");
        @signal[lifeTimeU2](type="simtime_t");
        @signal[lifeTime2s](type="long");
        @signal[lifeTime3s](type="long");
        @signal[lifeTime4s](type="long");
        @signal[numJobs](type="long");
        @statistic[numJobs](title="Numero di jobs eseguiti";record=vector?,count;interpolationmode=none);
        @statistic[lifeTime2s](title="Numero di job con lifeTime maggiore di 2s";record=vector?,count;interpolationmode=none);
        @statistic[lifeTime3s](title="Numero di job con lifeTime maggiore di 3s";record=vector?,count;interpolationmode=none);
        @statistic[lifeTime4s](title="Numero di job con lifeTime maggiore di 4s";record=vector?,count;interpolationmode=none);
        //@signal[totalQueueingTime](type="simtime_t");
        //@signal[totalDelayTime](type="simtime_t");
        @signal[totalServiceTime](type="simtime_t");
        @signal[totalServiceTimeU1](type="simtime_t");
        @signal[totalServiceTimeU2](type="simtime_t");
        //@signal[queuesVisited](type="long");
        //@signal[delaysVisited](type="long");
        //@signal[generation](type="long");
        @statistic[lifeTime](title="lifetime of arrived jobs";unit=s;record=vector,mean,max;interpolationmode=none);
        @statistic[lifeTimeU1](title="lifetime of arrived jobs U1";unit=s;record=vector,mean,max, min;interpolationmode=none);
        @statistic[lifeTimeU2](title="lifetime of arrived jobs U2";unit=s;record=vector,mean,max, min;interpolationmode=none);
        //@statistic[totalQueueingTime](title="the total time spent in queues by arrived jobs";unit=s;record=vector?,mean,max;interpolationmode=none);
        //@statistic[totalDelayTime](title="the total time spent in delay nodes by arrived jobs";unit=s;record=vector?,mean,max;interpolationmode=none);
        @statistic[totalServiceTime](title="the total time spent  by arrived jobs";unit=s;record=vector,mean,max,sum;interpolationmode=none);
        @statistic[totalServiceTimeU1](title="the total time spent  by arrived jobs U1";unit=s;record=vector,mean,max,sum;interpolationmode=none);
        @statistic[totalServiceTimeU2](title="the total time spent  by arrived jobs U2";unit=s;record=vector,mean,max,sum;interpolationmode=none);
       
        //@statistic[queuesVisited](title="the total number of queues visited by arrived jobs";record=vector?,mean,max;interpolationmode=none);
        //@statistic[delaysVisited](title="the total number of delays visited by arrived jobs";record=vector?,mean,max;interpolationmode=none);
        //@statistic[generation](title="the generation of the arrived jobs";record=vector?,mean,max;interpolationmode=none);
        bool keepJobs = default(false);
         // whether to keep the received jobs till the end of simulation
    gates:
        input in[];
}

