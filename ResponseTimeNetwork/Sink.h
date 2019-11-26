//
// This file is part of an OMNeT++/OMNEST simulation example.
//
// Copyright (C) 2006-2015 OpenSim Ltd.
//
// This file is distributed WITHOUT ANY WARRANTY. See the file
// `license' for details on this and other legal matters.
//

#ifndef __QUEUEING_SINK_H
#define __QUEUEING_SINK_H

#include "QueueingDefs.h"

namespace queueing {

/**
 * Consumes jobs; see NED file for more info.
 */
class QUEUEING_API Sink : public cSimpleModule
{
  private:
	simsignal_t lifeTimeSignal;
	simsignal_t lifeTimeU1Signal;
	simsignal_t lifeTimeU2Signal;
	simsignal_t lifeTime2sSignal;
	simsignal_t lifeTime3sSignal;
	simsignal_t lifeTime4sSignal;
	simsignal_t numJobsSignal;
    simsignal_t totalServiceTimeSignal;
    simsignal_t totalServiceTimeU1Signal;
    simsignal_t totalServiceTimeU2Signal;
    bool keepJobs;

  protected:
    virtual void initialize() override;
    virtual void handleMessage(cMessage *msg) override;
    virtual void finish() override;
};

}; //namespace

#endif

