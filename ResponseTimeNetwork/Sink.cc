//
// This file is part of an OMNeT++/OMNEST simulation example.
//
// Copyright (C) 2006-2015 OpenSim Ltd.
//
// This file is distributed WITHOUT ANY WARRANTY. See the file
// `license' for details on this and other legal matters.
//

#include "Sink.h"
#include "Job.h"

namespace queueing {

Define_Module(Sink);

void Sink::initialize()
{
    lifeTimeSignal = registerSignal("lifeTime");
    lifeTimeU1Signal = registerSignal("lifeTimeU1");
    lifeTimeU2Signal = registerSignal("lifeTimeU2");
    lifeTime2sSignal= registerSignal("lifeTime2s");
    lifeTime3sSignal= registerSignal("lifeTime3s");
    lifeTime4sSignal= registerSignal("lifeTime4s");
    numJobsSignal= registerSignal("numJobs");
    //totalQueueingTimeSignal = registerSignal("totalQueueingTime");
    //queuesVisitedSignal = registerSignal("queuesVisited");
    //totalServiceTimeSignal = registerSignal("totalServiceTime");
    //totalDelayTimeSignal = registerSignal("totalDelayTime");
    //delaysVisitedSignal = registerSignal("delaysVisited");
    //generationSignal = registerSignal("generation");
    keepJobs = par("keepJobs");

}

void Sink::handleMessage(cMessage *msg)
{
    Job *job = check_and_cast<Job *>(msg);

    if(job->getKind()==1){
        emit(lifeTimeU1Signal, simTime()- job->getCreationTime());
    }else{
        emit(lifeTimeU2Signal, simTime()- job->getCreationTime());
    }
    // gather statistics
    emit(lifeTimeSignal, simTime()- job->getCreationTime());

    if((job->getArrivalTime() - job->getCreationTime())>2.0){
        emit(lifeTime2sSignal, 1);
    }
    if((job->getArrivalTime() - job->getCreationTime())>3.0){
        emit(lifeTime3sSignal, 1);
    }
    if((job->getArrivalTime() - job->getCreationTime())>4.0){
        emit(lifeTime4sSignal, 1);
    }
    emit(numJobsSignal, 1);
    //emit(totalQueueingTimeSignal, job->getTotalQueueingTime());
    //emit(queuesVisitedSignal, job->getQueueCount());
    //emit(totalServiceTimeSignal, job->getTotalServiceTime());
    //emit(totalDelayTimeSignal, job->getTotalDelayTime());
    //emit(delaysVisitedSignal, job->getDelayCount());
    //emit(generationSignal, job->getGeneration());


    if (!keepJobs)
        delete msg;
}

void Sink::finish()
{

}; //namespace
}
