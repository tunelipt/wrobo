# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 2.7.10 |Anaconda 2.3.0 (32-bit)| (default, May 28 2015, 17:02:00) [MSC v.1500 32 bit (Intel)]
# From type library 'ComACRsrvr.dll'
# On Wed Nov 04 16:41:37 2015
'Parker ComACRsrvr'
makepy_version = '0.5.01'
python_version = 0x2070af0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{ED506EE7-375E-4BF3-BBAD-BA717E28A71D}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class IConfig(DispatchBaseClass):
	'IConfig Interface'
	CLSID = IID('{1A2C9178-A91B-47B2-A883-63835A732D57}')
	coclass_clsid = IID('{36682CAC-F0A6-45B3-AD99-A1A6F8A5B05F}')

	def AutoTune(self, fPGain=pythoncom.Missing, fIGain=pythoncom.Missing, fDGain=pythoncom.Missing):
		'Auto Tune'
		return self._ApplyTypes_(160, 1, (3, 0), ((16388, 2), (16388, 2), (16388, 2)), u'AutoTune', None,fPGain
			, fIGain, fDGain)

	def Connect(self, nTransport=defaultNamedNotOptArg, nIndex=defaultNamedNotOptArg):
		'Connect'
		return self._oleobj_.InvokeTypes(128, LCID, 1, (24, 0), ((3, 1), (3, 1)),nTransport
			, nIndex)

	def Disconnect(self):
		'Connect Offline'
		return self._oleobj_.InvokeTypes(99, LCID, 1, (24, 0), (),)

	def GetAniSetup(self, nAni=defaultNamedNotOptArg, nFilter=pythoncom.Missing):
		'Ani Setup'
		return self._ApplyTypes_(146, 1, (24, 0), ((3, 1), (16387, 2)), u'GetAniSetup', None,nAni
			, nFilter)

	def GetAxisFeedback(self, nAxis=defaultNamedNotOptArg, nPosnType=pythoncom.Missing, nPosnIndex=pythoncom.Missing, nPosnQuad=pythoncom.Missing
			, nPosnSrc=pythoncom.Missing, nPosnPkg=pythoncom.Missing, fPosnRes=pythoncom.Missing, nPosSmper=pythoncom.Missing, nNegSmper=pythoncom.Missing
			, nVelType=pythoncom.Missing, nVelIndex=pythoncom.Missing, nVelQuad=pythoncom.Missing, nVelSrc=pythoncom.Missing, nVelPkg=pythoncom.Missing
			, fVelRes=pythoncom.Missing):
		'Setup Axis Feedback'
		return self._ApplyTypes_(110, 1, (24, 0), ((3, 1), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16388, 2), (16388, 2), (16388, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16388, 2)), u'GetAxisFeedback', None,nAxis
			, nPosnType, nPosnIndex, nPosnQuad, nPosnSrc, nPosnPkg
			, fPosnRes, nPosSmper, nNegSmper, nVelType, nVelIndex
			, nVelQuad, nVelSrc, nVelPkg, fVelRes)

	def GetAxisGains(self, nAxis=defaultNamedNotOptArg, fPropGain=pythoncom.Missing, fIntGain=pythoncom.Missing, fIntLimit=pythoncom.Missing
			, fIntDelay=pythoncom.Missing, fDerGain=pythoncom.Missing, fDerWidth=pythoncom.Missing, fFeedFVel=pythoncom.Missing, fFeedFAcc=pythoncom.Missing
			, fTorqLimit=pythoncom.Missing, fFBackVel=pythoncom.Missing):
		'Axis Gains'
		return self._ApplyTypes_(135, 1, (24, 0), ((3, 1), (16388, 2), (16388, 2), (16388, 2), (16388, 2), (16388, 2), (16388, 2), (16388, 2), (16388, 2), (16388, 2), (16388, 2)), u'GetAxisGains', None,nAxis
			, fPropGain, fIntGain, fIntLimit, fIntDelay, fDerGain
			, fDerWidth, fFeedFVel, fFeedFAcc, fTorqLimit, fFBackVel
			)

	def GetAxisHome(self, nAxis=defaultNamedNotOptArg, fHomAcc=pythoncom.Missing, fHomVel=pythoncom.Missing, fHomDec=pythoncom.Missing
			, fHomJrk=pythoncom.Missing, fHomFinV=pythoncom.Missing, nHomBackup=pythoncom.Missing, nHomFinDir=pythoncom.Missing, nHomEdge=pythoncom.Missing):
		'Axis Home Settings'
		return self._ApplyTypes_(140, 1, (24, 0), ((3, 1), (16388, 2), (16388, 2), (16388, 2), (16388, 2), (16388, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetAxisHome', None,nAxis
			, fHomAcc, fHomVel, fHomDec, fHomJrk, fHomFinV
			, nHomBackup, nHomFinDir, nHomEdge)

	def GetAxisIO(self, nAxis=defaultNamedNotOptArg, nHwPosLimit=pythoncom.Missing, nHwPosLimitLevel=pythoncom.Missing, nHwNegLimit=pythoncom.Missing
			, nHwNegLimitLevel=pythoncom.Missing, nHwHomeLimit=pythoncom.Missing, nHwHomeLevel=pythoncom.Missing, nDriveFault=pythoncom.Missing, nDriveFaultLevel=pythoncom.Missing
			, nDriveEnable=pythoncom.Missing, nDriveEnableLevel=pythoncom.Missing, nDriveReset=pythoncom.Missing, nDriveResetLevel=pythoncom.Missing, bOnKill=pythoncom.Missing):
		'Setup Axis IO'
		return self._ApplyTypes_(112, 1, (24, 0), ((3, 1), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16395, 2)), u'GetAxisIO', None,nAxis
			, nHwPosLimit, nHwPosLimitLevel, nHwNegLimit, nHwNegLimitLevel, nHwHomeLimit
			, nHwHomeLevel, nDriveFault, nDriveFaultLevel, nDriveEnable, nDriveEnableLevel
			, nDriveReset, nDriveResetLevel, bOnKill)

	def GetAxisJog(self, nAxis=defaultNamedNotOptArg, fJogAcc=pythoncom.Missing, fJogVel=pythoncom.Missing, fJogDec=pythoncom.Missing
			, fJogJrk=pythoncom.Missing, fJogPosLimit=pythoncom.Missing, fJogNegLimit=pythoncom.Missing, bJogEnableLimit=pythoncom.Missing, bJogLockout=pythoncom.Missing):
		'Axis Jog Settings'
		return self._ApplyTypes_(137, 1, (24, 0), ((3, 1), (16388, 2), (16388, 2), (16388, 2), (16388, 2), (16388, 2), (16388, 2), (16395, 2), (16395, 2)), u'GetAxisJog', None,nAxis
			, fJogAcc, fJogVel, fJogDec, fJogJrk, fJogPosLimit
			, fJogNegLimit, bJogEnableLimit, bJogLockout)

	def GetAxisLimits(self, nAxis=defaultNamedNotOptArg, bHwPos=pythoncom.Missing, bHwNeg=pythoncom.Missing, fHwLimitStp=pythoncom.Missing
			, bHwHome=pythoncom.Missing, bSwPos=pythoncom.Missing, fSwPosValue=pythoncom.Missing, bSwNeg=pythoncom.Missing, fSwNegValue=pythoncom.Missing
			, fSwLimitStp=pythoncom.Missing, fVelLimit=pythoncom.Missing):
		'Setup Axis Limits'
		return self._ApplyTypes_(114, 1, (24, 0), ((3, 1), (16395, 2), (16395, 2), (16388, 2), (16395, 2), (16395, 2), (16388, 2), (16395, 2), (16388, 2), (16388, 2), (16388, 2)), u'GetAxisLimits', None,nAxis
			, bHwPos, bHwNeg, fHwLimitStp, bHwHome, bSwPos
			, fSwPosValue, bSwNeg, fSwNegValue, fSwLimitStp, fVelLimit
			)

	def GetAxisProfile(self, nAxis=defaultNamedNotOptArg, nProfile=pythoncom.Missing, bstrName=pythoncom.Missing):
		'Link Axis to Profile'
		return self._ApplyTypes_(116, 1, (24, 0), ((3, 1), (16387, 2), (16392, 2)), u'GetAxisProfile', None,nAxis
			, nProfile, bstrName)

	def GetAxisScale(self, nAxis=defaultNamedNotOptArg, nUnits=pythoncom.Missing, bstrUnitsName=pythoncom.Missing, nTrans=pythoncom.Missing
			, fTransFactor=pythoncom.Missing, nReducer=pythoncom.Missing, fRedFactor1=pythoncom.Missing, fRedFactor2=pythoncom.Missing, fRedFactor3=pythoncom.Missing
			, fRedFactor4=pythoncom.Missing, fSclFactor=pythoncom.Missing, fPPU=pythoncom.Missing, nLoadOrder=pythoncom.Missing, fLoadAmt=pythoncom.Missing
			, bstrPartNbr=pythoncom.Missing):
		'Setup Axis Scale'
		return self._ApplyTypes_(122, 1, (24, 0), ((3, 1), (16387, 2), (16392, 2), (16387, 2), (16388, 2), (16387, 2), (16388, 2), (16388, 2), (16388, 2), (16388, 2), (16388, 2), (16389, 2), (16387, 2), (16388, 2), (16392, 2)), u'GetAxisScale', None,nAxis
			, nUnits, bstrUnitsName, nTrans, fTransFactor, nReducer
			, fRedFactor1, fRedFactor2, fRedFactor3, fRedFactor4, fSclFactor
			, fPPU, nLoadOrder, fLoadAmt, bstrPartNbr)

	def GetAxisSignal(self, nAxis=defaultNamedNotOptArg, nSignalType=pythoncom.Missing, nSignalIndex=pythoncom.Missing, nStepMode=pythoncom.Missing
			, nDrive=pythoncom.Missing, nDriveRes=pythoncom.Missing, nMotor=pythoncom.Missing, nMotorPkg=pythoncom.Missing, nGearHead=pythoncom.Missing):
		'Setup Axis Signals'
		return self._ApplyTypes_(124, 1, (24, 0), ((3, 1), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetAxisSignal', None,nAxis
			, nSignalType, nSignalIndex, nStepMode, nDrive, nDriveRes
			, nMotor, nMotorPkg, nGearHead)

	def GetAxisSsiData(self, nAxis=defaultNamedNotOptArg, nPosnClock=pythoncom.Missing, nPosnDST=pythoncom.Missing, nPosnWidth=pythoncom.Missing
			, nPosnLimit=pythoncom.Missing, nVelClock=pythoncom.Missing, nVelDST=pythoncom.Missing, nVelWidth=pythoncom.Missing, nVelLimit=pythoncom.Missing):
		'Axis SSI Data'
		return self._ApplyTypes_(142, 1, (24, 0), ((3, 1), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetAxisSsiData', None,nAxis
			, nPosnClock, nPosnDST, nPosnWidth, nPosnLimit, nVelClock
			, nVelDST, nVelWidth, nVelLimit)

	def GetCANnode(self, nNode=defaultNamedNotOptArg, nNodeID=pythoncom.Missing, nDInput=pythoncom.Missing, nDOutput=pythoncom.Missing
			, nAInput=pythoncom.Missing, nAOutput=pythoncom.Missing, nType=pythoncom.Missing, nTimeBase=pythoncom.Missing, nTimeDPoint=pythoncom.Missing
			, nTimeAPoint=pythoncom.Missing):
		'CANopen cyclic period'
		return self._ApplyTypes_(130, 1, (24, 0), ((3, 1), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetCANnode', None,nNode
			, nNodeID, nDInput, nDOutput, nAInput, nAOutput
			, nType, nTimeBase, nTimeDPoint, nTimeAPoint)

	def GetCANopen(self, nMaster=pythoncom.Missing, nBitRate=pythoncom.Missing, nPeriod=pythoncom.Missing, nNodes=pythoncom.Missing):
		'Setup CANopen'
		return self._ApplyTypes_(126, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetCANopen', None,nMaster
			, nBitRate, nPeriod, nNodes)

	def GetDimPLC(self, nIndex=defaultNamedNotOptArg):
		'Get PLC Memory'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (3, 0), ((3, 1),),nIndex
			)

	def GetDimPLCDefault(self, nIndex=defaultNamedNotOptArg):
		'Get PLC Memory Default'
		return self._oleobj_.InvokeTypes(104, LCID, 1, (3, 0), ((3, 1),),nIndex
			)

	def GetDimProg(self, nIndex=defaultNamedNotOptArg):
		'Get Program Memory'
		return self._oleobj_.InvokeTypes(100, LCID, 1, (3, 0), ((3, 1),),nIndex
			)

	def GetDimProgDefault(self, nIndex=defaultNamedNotOptArg):
		'Get Program Memory Default'
		return self._oleobj_.InvokeTypes(101, LCID, 1, (3, 0), ((3, 1),),nIndex
			)

	def GetEPLAdvancedDriveMotorData(self, nAxis=defaultNamedNotOptArg, nMotorPackageSel=pythoncom.Missing, strMotorPackage=pythoncom.Missing, nPosFeedbackPackage=pythoncom.Missing
			, strMotorRatedSpeed=pythoncom.Missing, strMotorPolePairs=pythoncom.Missing, strMotorRotorInertia=pythoncom.Missing, strMotorDamping=pythoncom.Missing, strMotorThermalTimeConstant=pythoncom.Missing
			, strWindingThermalTimeConstant=pythoncom.Missing, strWindingThermalResistance=pythoncom.Missing, strMotorAmbientTemp=pythoncom.Missing, strMaxMotorWindingTemp=pythoncom.Missing, strKe=pythoncom.Missing
			, strContCurrent=pythoncom.Missing, strContCurrentDerating=pythoncom.Missing, strPeakCurrent=pythoncom.Missing, strWindingResistance=pythoncom.Missing, strMinInductance=pythoncom.Missing
			, strMaxInductance=pythoncom.Missing, strFeedbackResolution=pythoncom.Missing, nFeedbackTypeSel=pythoncom.Missing, bInvertHallSignals=pythoncom.Missing):
		'EPL Advanced Drive Motor Settings'
		return self._ApplyTypes_(156, 1, (24, 0), ((3, 1), (16387, 2), (16392, 2), (16387, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16387, 2), (16395, 2)), u'GetEPLAdvancedDriveMotorData', None,nAxis
			, nMotorPackageSel, strMotorPackage, nPosFeedbackPackage, strMotorRatedSpeed, strMotorPolePairs
			, strMotorRotorInertia, strMotorDamping, strMotorThermalTimeConstant, strWindingThermalTimeConstant, strWindingThermalResistance
			, strMotorAmbientTemp, strMaxMotorWindingTemp, strKe, strContCurrent, strContCurrentDerating
			, strPeakCurrent, strWindingResistance, strMinInductance, strMaxInductance, strFeedbackResolution
			, nFeedbackTypeSel, bInvertHallSignals)

	def GetEPLData(self, nNumberOfControlledNodes=pythoncom.Missing):
		'Setup EPL'
		return self._ApplyTypes_(150, 1, (24, 0), ((16387, 2),), u'GetEPLData', None,nNumberOfControlledNodes
			)

	def GetEPLDriveModeData(self, nAxis=defaultNamedNotOptArg, nDriveControlMode=pythoncom.Missing, bEnableCurrentFoldback=pythoncom.Missing, nCommutationSel=pythoncom.Missing
			, nSwitchingFrequencySel=pythoncom.Missing, bstrSwitchingFrequency=pythoncom.Missing, bstrTorqueLimit=pythoncom.Missing, bstrTorqueScaling=pythoncom.Missing, bstrVelocityLimit=pythoncom.Missing
			, bstrVelocityScaling=pythoncom.Missing, bstrProportionalGain=pythoncom.Missing, bstrIntegralGain=pythoncom.Missing, bstrIntegralLimit=pythoncom.Missing, bstrBandwidth=pythoncom.Missing
			, bIAuto=pythoncom.Missing, bstrPositionProportionalGain=pythoncom.Missing, bstrPositionIntegralGain=pythoncom.Missing, bstrPositionIntegralLimit=pythoncom.Missing, bstrPositionVelocityGain=pythoncom.Missing
			, bstrPositionVelocityFeedforwardGain=pythoncom.Missing, bstrVelocityProportionalGain=pythoncom.Missing, bstrVelocityIntegralGain=pythoncom.Missing, bstrVelocityIntegralLimit=pythoncom.Missing):
		'EPL Drive Mode Settings'
		return self._ApplyTypes_(163, 1, (24, 0), ((3, 1), (16387, 2), (16395, 2), (16387, 2), (16387, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16395, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2), (16392, 2)), u'GetEPLDriveModeData', None,nAxis
			, nDriveControlMode, bEnableCurrentFoldback, nCommutationSel, nSwitchingFrequencySel, bstrSwitchingFrequency
			, bstrTorqueLimit, bstrTorqueScaling, bstrVelocityLimit, bstrVelocityScaling, bstrProportionalGain
			, bstrIntegralGain, bstrIntegralLimit, bstrBandwidth, bIAuto, bstrPositionProportionalGain
			, bstrPositionIntegralGain, bstrPositionIntegralLimit, bstrPositionVelocityGain, bstrPositionVelocityFeedforwardGain, bstrVelocityProportionalGain
			, bstrVelocityIntegralGain, bstrVelocityIntegralLimit)

	def GetEPLDriveMotorData(self, nAxis=defaultNamedNotOptArg, bIsAriesEPLSelected=pythoncom.Missing, nSeriesSel=pythoncom.Missing, nFrameSel=pythoncom.Missing
			, nStackSel=pythoncom.Missing, nWindingSel=pythoncom.Missing, nFeedbackSel=pythoncom.Missing, nCustomPartNumberSel=pythoncom.Missing, nBaseSeriesSel=pythoncom.Missing
			, strUserDefinedPartNumber=pythoncom.Missing, nCustomWindingSel=pythoncom.Missing, nCoolingSel=pythoncom.Missing, nHeatSink=pythoncom.Missing, bAdvancedSel=pythoncom.Missing
			, strFullPartNumber=pythoncom.Missing, strHeatSink=pythoncom.Missing, strCustomWindingNumber=pythoncom.Missing, bIsCustomResolution=pythoncom.Missing):
		'EPL Drive Motor Settings'
		return self._ApplyTypes_(154, 1, (24, 0), ((3, 1), (16395, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16392, 2), (16387, 2), (16387, 2), (16387, 2), (16395, 2), (16392, 2), (16392, 2), (16392, 2), (16395, 2)), u'GetEPLDriveMotorData', None,nAxis
			, bIsAriesEPLSelected, nSeriesSel, nFrameSel, nStackSel, nWindingSel
			, nFeedbackSel, nCustomPartNumberSel, nBaseSeriesSel, strUserDefinedPartNumber, nCustomWindingSel
			, nCoolingSel, nHeatSink, bAdvancedSel, strFullPartNumber, strHeatSink
			, strCustomWindingNumber, bIsCustomResolution)

	def GetEPLNodeData(self, nAxis=defaultNamedNotOptArg, nNodeID=pythoncom.Missing, nMultiplexedCycleNumber=pythoncom.Missing, nDriveMode=pythoncom.Missing
			, nTCPIPPortNumber=pythoncom.Missing, nReserved1=pythoncom.Missing, nReserved2=pythoncom.Missing):
		'EPL Settings'
		return self._ApplyTypes_(152, 1, (24, 0), ((3, 1), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetEPLNodeData', None,nAxis
			, nNodeID, nMultiplexedCycleNumber, nDriveMode, nTCPIPPortNumber, nReserved1
			, nReserved2)

	def GetEPLPeriod(self, dEPLPeriod=pythoncom.Missing):
		'EPL Period'
		return self._ApplyTypes_(161, 1, (24, 0), ((16388, 2),), u'GetEPLPeriod', None,dEPLPeriod
			)

	def GetFaultOutputThermalInputData(self, nAxis=defaultNamedNotOptArg, bEnableFaultOnDriveDisable=pythoncom.Missing, strOutputBrakeDelay=pythoncom.Missing, bDisableMotorThermalSensor=pythoncom.Missing
			, nMotorThermalSensorTypeSel=pythoncom.Missing, nMotorThermalSensorConstructionSel=pythoncom.Missing):
		'Fault Output Thermal Input Settings'
		return self._ApplyTypes_(158, 1, (24, 0), ((3, 1), (16395, 2), (16392, 2), (16395, 2), (16387, 2), (16387, 2)), u'GetFaultOutputThermalInputData', None,nAxis
			, bEnableFaultOnDriveDisable, strOutputBrakeDelay, bDisableMotorThermalSensor, nMotorThermalSensorTypeSel, nMotorThermalSensorConstructionSel
			)

	def GetSetupHW(self, nCard=pythoncom.Missing, nEncoder=pythoncom.Missing, nServo1=pythoncom.Missing, nStepper1=pythoncom.Missing
			, nServo2=pythoncom.Missing, nStepper2=pythoncom.Missing, nAnalog=pythoncom.Missing, nAnalogMode=pythoncom.Missing, nIOMode=pythoncom.Missing
			, nExpandedIO=pythoncom.Missing):
		'Hardware Setup'
		return self._ApplyTypes_(106, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetSetupHW', None,nCard
			, nEncoder, nServo1, nStepper1, nServo2, nStepper2
			, nAnalog, nAnalogMode, nIOMode, nExpandedIO)

	def GetSetupHWex(self, nEncoder=pythoncom.Missing, nServo1=pythoncom.Missing, nStepper1=pythoncom.Missing, nServo2=pythoncom.Missing
			, nStepper2=pythoncom.Missing, nAnalog=pythoncom.Missing, nAnalogMode=pythoncom.Missing):
		'Hardware Setup Ex'
		return self._ApplyTypes_(108, 1, (24, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2), (16387, 2)), u'GetSetupHWex', None,nEncoder
			, nServo1, nStepper1, nServo2, nStepper2, nAnalog
			, nAnalogMode)

	def GetSetupProfile(self, nProfile=defaultNamedNotOptArg, fVecVel=pythoncom.Missing, fVecAcc=pythoncom.Missing, fRampSTP=pythoncom.Missing
			, fRampDEC=pythoncom.Missing, bSCurve=pythoncom.Missing, bEstopHWLimit=pythoncom.Missing, bEstopSWLimit=pythoncom.Missing, nSysCfgType=pythoncom.Missing
			, bstrSysPartNbr=pythoncom.Missing):
		'Setup Motion Profiles'
		return self._ApplyTypes_(118, 1, (24, 0), ((3, 1), (16388, 2), (16388, 2), (16388, 2), (16388, 2), (16395, 2), (16395, 2), (16395, 2), (16387, 2), (16392, 2)), u'GetSetupProfile', None,nProfile
			, fVecVel, fVecAcc, fRampSTP, fRampDEC, bSCurve
			, bEstopHWLimit, bEstopSWLimit, nSysCfgType, bstrSysPartNbr)

	def GetUserData(self, bstrBody=pythoncom.Missing):
		'User Data'
		return self._ApplyTypes_(144, 1, (24, 0), ((16392, 2),), u'GetUserData', None,bstrBody
			)

	def LoadAriesConfig(self, bstrFile=defaultNamedNotOptArg):
		'Load Aries Configuration'
		return self._oleobj_.InvokeTypes(148, LCID, 1, (24, 0), ((8, 1),),bstrFile
			)

	def LoadConfig(self, bstrPath=defaultNamedNotOptArg):
		'Load Configuration'
		return self._oleobj_.InvokeTypes(121, LCID, 1, (24, 0), ((8, 1),),bstrPath
			)

	def PutAniSetup(self, nAni=defaultNamedNotOptArg, nFilter=defaultNamedNotOptArg):
		'Ani Setup'
		return self._oleobj_.InvokeTypes(147, LCID, 1, (24, 0), ((3, 1), (3, 1)),nAni
			, nFilter)

	def PutAxisFeedback(self, nAxis=defaultNamedNotOptArg, nPosnType=defaultNamedNotOptArg, nPosnIndex=defaultNamedNotOptArg, nPosnQuad=defaultNamedNotOptArg
			, nPosnSrc=defaultNamedNotOptArg, nPosnPkg=defaultNamedNotOptArg, fPosnRes=defaultNamedNotOptArg, nPosSmper=defaultNamedNotOptArg, nNegSmper=defaultNamedNotOptArg
			, nVelType=defaultNamedNotOptArg, nVelIndex=defaultNamedNotOptArg, nVelQuad=defaultNamedNotOptArg, nVelSrc=defaultNamedNotOptArg, nVelPkg=defaultNamedNotOptArg
			, fVelRes=defaultNamedNotOptArg):
		'Setup Axis Feedback'
		return self._oleobj_.InvokeTypes(111, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (4, 1), (4, 1), (4, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (4, 1)),nAxis
			, nPosnType, nPosnIndex, nPosnQuad, nPosnSrc, nPosnPkg
			, fPosnRes, nPosSmper, nNegSmper, nVelType, nVelIndex
			, nVelQuad, nVelSrc, nVelPkg, fVelRes)

	def PutAxisGains(self, nAxis=defaultNamedNotOptArg, fPropGain=defaultNamedNotOptArg, fIntGain=defaultNamedNotOptArg, fIntLimit=defaultNamedNotOptArg
			, fIntDelay=defaultNamedNotOptArg, fDerGain=defaultNamedNotOptArg, fDerWidth=defaultNamedNotOptArg, fFeedFVel=defaultNamedNotOptArg, fFeedFAcc=defaultNamedNotOptArg
			, fTorqLimit=defaultNamedNotOptArg, fFBackVel=defaultNamedNotOptArg):
		'Axis Gains'
		return self._oleobj_.InvokeTypes(136, LCID, 1, (24, 0), ((3, 1), (4, 1), (4, 1), (4, 1), (4, 1), (4, 1), (4, 1), (4, 1), (4, 1), (4, 1), (4, 1)),nAxis
			, fPropGain, fIntGain, fIntLimit, fIntDelay, fDerGain
			, fDerWidth, fFeedFVel, fFeedFAcc, fTorqLimit, fFBackVel
			)

	def PutAxisHome(self, nAxis=defaultNamedNotOptArg, fHomAcc=defaultNamedNotOptArg, fHomVel=defaultNamedNotOptArg, fHomDec=defaultNamedNotOptArg
			, fHomJrk=defaultNamedNotOptArg, fHomFinV=defaultNamedNotOptArg, nHomBackup=defaultNamedNotOptArg, nHomFinDir=defaultNamedNotOptArg, nHomEdge=defaultNamedNotOptArg):
		'Axis Home Settings'
		return self._oleobj_.InvokeTypes(141, LCID, 1, (24, 0), ((3, 1), (4, 1), (4, 1), (4, 1), (4, 1), (4, 1), (3, 1), (3, 1), (3, 1)),nAxis
			, fHomAcc, fHomVel, fHomDec, fHomJrk, fHomFinV
			, nHomBackup, nHomFinDir, nHomEdge)

	def PutAxisIO(self, nAxis=defaultNamedNotOptArg, nHwPosLimit=defaultNamedNotOptArg, nHwPosLimitLevel=defaultNamedNotOptArg, nHwNegLimit=defaultNamedNotOptArg
			, nHwNegLimitLevel=defaultNamedNotOptArg, nHwHomeLimit=defaultNamedNotOptArg, nHwHomeLevel=defaultNamedNotOptArg, nDriveFault=defaultNamedNotOptArg, nDriveFaultLevel=defaultNamedNotOptArg
			, nDriveEnable=defaultNamedNotOptArg, nDriveEnableLevel=defaultNamedNotOptArg, nDriveReset=defaultNamedNotOptArg, nDriveResetLevel=defaultNamedNotOptArg, bOnKill=defaultNamedNotOptArg):
		'Setup Axis IO'
		return self._oleobj_.InvokeTypes(113, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (11, 1)),nAxis
			, nHwPosLimit, nHwPosLimitLevel, nHwNegLimit, nHwNegLimitLevel, nHwHomeLimit
			, nHwHomeLevel, nDriveFault, nDriveFaultLevel, nDriveEnable, nDriveEnableLevel
			, nDriveReset, nDriveResetLevel, bOnKill)

	def PutAxisJog(self, nAxis=defaultNamedNotOptArg, fJogAcc=defaultNamedNotOptArg, fJogVel=defaultNamedNotOptArg, fJogDec=defaultNamedNotOptArg
			, fJogJrk=defaultNamedNotOptArg, fJogPosLimit=defaultNamedNotOptArg, fJogNegLimit=defaultNamedNotOptArg, bJogEnableLimit=defaultNamedNotOptArg, bJogLockout=defaultNamedNotOptArg):
		'Axis Jog Settings'
		return self._oleobj_.InvokeTypes(138, LCID, 1, (24, 0), ((3, 1), (4, 1), (4, 1), (4, 1), (4, 1), (4, 1), (4, 1), (11, 1), (11, 1)),nAxis
			, fJogAcc, fJogVel, fJogDec, fJogJrk, fJogPosLimit
			, fJogNegLimit, bJogEnableLimit, bJogLockout)

	def PutAxisLimits(self, nAxis=defaultNamedNotOptArg, bHwPos=defaultNamedNotOptArg, bHwNeg=defaultNamedNotOptArg, fHwLimitStp=defaultNamedNotOptArg
			, bHwHome=defaultNamedNotOptArg, bSwPos=defaultNamedNotOptArg, fSwPosValue=defaultNamedNotOptArg, bSwNeg=defaultNamedNotOptArg, fSwNegValue=defaultNamedNotOptArg
			, fSwLimitStp=defaultNamedNotOptArg, fVelLimit=defaultNamedNotOptArg):
		'Setup Axis Limits'
		return self._oleobj_.InvokeTypes(115, LCID, 1, (24, 0), ((3, 1), (11, 1), (11, 1), (4, 1), (11, 1), (11, 1), (4, 1), (11, 1), (4, 1), (4, 1), (4, 1)),nAxis
			, bHwPos, bHwNeg, fHwLimitStp, bHwHome, bSwPos
			, fSwPosValue, bSwNeg, fSwNegValue, fSwLimitStp, fVelLimit
			)

	def PutAxisProfile(self, nAxis=defaultNamedNotOptArg, nProfile=defaultNamedNotOptArg, bstrName=defaultNamedNotOptArg):
		'Link Axis to Profile'
		return self._oleobj_.InvokeTypes(117, LCID, 1, (24, 0), ((3, 1), (3, 1), (8, 1)),nAxis
			, nProfile, bstrName)

	def PutAxisScale(self, nAxis=defaultNamedNotOptArg, nUnits=defaultNamedNotOptArg, bstrUnitsName=defaultNamedNotOptArg, nTrans=defaultNamedNotOptArg
			, fTransFactor=defaultNamedNotOptArg, nReducer=defaultNamedNotOptArg, fRedFactor1=defaultNamedNotOptArg, fRedFactor2=defaultNamedNotOptArg, fRedFactor3=defaultNamedNotOptArg
			, fRedFactor4=defaultNamedNotOptArg, fSclFactor=defaultNamedNotOptArg, fPPU=defaultNamedNotOptArg, nLoadOrder=defaultNamedNotOptArg, fLoadAmt=defaultNamedNotOptArg
			, bstrPartNbr=defaultNamedNotOptArg):
		'Setup Axis Scale'
		return self._oleobj_.InvokeTypes(123, LCID, 1, (24, 0), ((3, 1), (3, 1), (8, 1), (3, 1), (4, 1), (3, 1), (4, 1), (4, 1), (4, 1), (4, 1), (4, 1), (5, 1), (3, 1), (4, 1), (8, 1)),nAxis
			, nUnits, bstrUnitsName, nTrans, fTransFactor, nReducer
			, fRedFactor1, fRedFactor2, fRedFactor3, fRedFactor4, fSclFactor
			, fPPU, nLoadOrder, fLoadAmt, bstrPartNbr)

	def PutAxisSignal(self, nAxis=defaultNamedNotOptArg, nSignalType=defaultNamedNotOptArg, nSignalIndex=defaultNamedNotOptArg, nStepMode=defaultNamedNotOptArg
			, nDrive=defaultNamedNotOptArg, nDriveRes=defaultNamedNotOptArg, nMotor=defaultNamedNotOptArg, nMotorPkg=defaultNamedNotOptArg, nGearHead=defaultNamedNotOptArg):
		'Setup Axis Signals'
		return self._oleobj_.InvokeTypes(125, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)),nAxis
			, nSignalType, nSignalIndex, nStepMode, nDrive, nDriveRes
			, nMotor, nMotorPkg, nGearHead)

	def PutAxisSsiData(self, nAxis=defaultNamedNotOptArg, nPosnClock=defaultNamedNotOptArg, nPosnDST=defaultNamedNotOptArg, nPosnWidth=defaultNamedNotOptArg
			, nPosnLimit=defaultNamedNotOptArg, nVelClock=defaultNamedNotOptArg, nVelDST=defaultNamedNotOptArg, nVelWidth=defaultNamedNotOptArg, nVelLimit=defaultNamedNotOptArg):
		'Axis SSI Data'
		return self._oleobj_.InvokeTypes(143, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)),nAxis
			, nPosnClock, nPosnDST, nPosnWidth, nPosnLimit, nVelClock
			, nVelDST, nVelWidth, nVelLimit)

	def PutCANnode(self, nNode=defaultNamedNotOptArg, nNodeID=defaultNamedNotOptArg, nDInput=defaultNamedNotOptArg, nDOutput=defaultNamedNotOptArg
			, nAInput=defaultNamedNotOptArg, nAOutput=defaultNamedNotOptArg, nType=defaultNamedNotOptArg, nTimeBase=defaultNamedNotOptArg, nTimeDPoint=defaultNamedNotOptArg
			, nTimeAPoint=defaultNamedNotOptArg):
		'CANopen cyclic period'
		return self._oleobj_.InvokeTypes(131, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)),nNode
			, nNodeID, nDInput, nDOutput, nAInput, nAOutput
			, nType, nTimeBase, nTimeDPoint, nTimeAPoint)

	def PutCANopen(self, nMaster=defaultNamedNotOptArg, nBitRate=defaultNamedNotOptArg, nPeriod=defaultNamedNotOptArg, nNodes=defaultNamedNotOptArg):
		'Setup CANopen'
		return self._oleobj_.InvokeTypes(127, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),nMaster
			, nBitRate, nPeriod, nNodes)

	def PutDimPLCDefault(self, nIndex=defaultNamedNotOptArg, nMemory=defaultNamedNotOptArg):
		'Put PLC Memory Default'
		return self._oleobj_.InvokeTypes(105, LCID, 1, (24, 0), ((3, 1), (3, 1)),nIndex
			, nMemory)

	def PutDimProgDefault(self, nIndex=defaultNamedNotOptArg, nMemory=defaultNamedNotOptArg):
		'Put Program Memory Default'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((3, 1), (3, 1)),nIndex
			, nMemory)

	def PutEPLAdvancedDriveMotorData(self, nAxis=defaultNamedNotOptArg, nMotorPackageSel=defaultNamedNotOptArg, strMotorPackage=defaultNamedNotOptArg, nPosFeedbackPackage=defaultNamedNotOptArg
			, strMotorRatedSpeed=defaultNamedNotOptArg, strMotorPolePairs=defaultNamedNotOptArg, strMotorRotorInertia=defaultNamedNotOptArg, strMotorDamping=defaultNamedNotOptArg, strMotorThermalTimeConstant=defaultNamedNotOptArg
			, strWindingThermalTimeConstant=defaultNamedNotOptArg, strWindingThermalResistance=defaultNamedNotOptArg, strMotorAmbientTemp=defaultNamedNotOptArg, strMaxMotorWindingTemp=defaultNamedNotOptArg, strKe=defaultNamedNotOptArg
			, strContCurrent=defaultNamedNotOptArg, strContCurrentDerating=defaultNamedNotOptArg, strPeakCurrent=defaultNamedNotOptArg, strWindingResistance=defaultNamedNotOptArg, strMinInductance=defaultNamedNotOptArg
			, strMaxInductance=defaultNamedNotOptArg, strFeedbackResolution=defaultNamedNotOptArg, nFeedbackTypeSel=defaultNamedNotOptArg, bInvertHallSignals=defaultNamedNotOptArg):
		'EPL Advanced Drive Motor Settings'
		return self._oleobj_.InvokeTypes(157, LCID, 1, (24, 0), ((3, 1), (3, 1), (8, 1), (3, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (3, 1), (11, 1)),nAxis
			, nMotorPackageSel, strMotorPackage, nPosFeedbackPackage, strMotorRatedSpeed, strMotorPolePairs
			, strMotorRotorInertia, strMotorDamping, strMotorThermalTimeConstant, strWindingThermalTimeConstant, strWindingThermalResistance
			, strMotorAmbientTemp, strMaxMotorWindingTemp, strKe, strContCurrent, strContCurrentDerating
			, strPeakCurrent, strWindingResistance, strMinInductance, strMaxInductance, strFeedbackResolution
			, nFeedbackTypeSel, bInvertHallSignals)

	def PutEPLData(self, nTotalTraditionalAxes=defaultNamedNotOptArg, nNumberOfControlledNodes=defaultNamedNotOptArg):
		'Setup EPL'
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), ((3, 1), (3, 1)),nTotalTraditionalAxes
			, nNumberOfControlledNodes)

	def PutEPLDriveModeData(self, nAxis=defaultNamedNotOptArg, nDriveControlMode=defaultNamedNotOptArg, bEnableCurrentFoldback=defaultNamedNotOptArg, nCommutationSel=defaultNamedNotOptArg
			, nSwitchingFrequencySel=defaultNamedNotOptArg, bstrSwitchingFrequency=defaultNamedNotOptArg, bstrTorqueLimit=defaultNamedNotOptArg, bstrTorqueScaling=defaultNamedNotOptArg, bstrVelocityLimit=defaultNamedNotOptArg
			, bstrVelocityScaling=defaultNamedNotOptArg, bstrProportionalGain=defaultNamedNotOptArg, bstrIntegralGain=defaultNamedNotOptArg, bstrIntegralLimit=defaultNamedNotOptArg, bstrBandwidth=defaultNamedNotOptArg
			, bIAuto=defaultNamedNotOptArg, bstrPositionProportionalGain=defaultNamedNotOptArg, bstrPositionIntegralGain=defaultNamedNotOptArg, bstrPositionIntegralLimit=defaultNamedNotOptArg, bstrPositionVelocityGain=defaultNamedNotOptArg
			, bstrPositionVelocityFeedforwardGain=defaultNamedNotOptArg, bstrVelocityProportionalGain=defaultNamedNotOptArg, bstrVelocityIntegralGain=defaultNamedNotOptArg, bstrVelocityIntegralLimit=defaultNamedNotOptArg):
		'EPL Drive Mode Settings'
		return self._oleobj_.InvokeTypes(164, LCID, 1, (24, 0), ((3, 1), (3, 1), (11, 1), (3, 1), (3, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (11, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1)),nAxis
			, nDriveControlMode, bEnableCurrentFoldback, nCommutationSel, nSwitchingFrequencySel, bstrSwitchingFrequency
			, bstrTorqueLimit, bstrTorqueScaling, bstrVelocityLimit, bstrVelocityScaling, bstrProportionalGain
			, bstrIntegralGain, bstrIntegralLimit, bstrBandwidth, bIAuto, bstrPositionProportionalGain
			, bstrPositionIntegralGain, bstrPositionIntegralLimit, bstrPositionVelocityGain, bstrPositionVelocityFeedforwardGain, bstrVelocityProportionalGain
			, bstrVelocityIntegralGain, bstrVelocityIntegralLimit)

	def PutEPLDriveMotorData(self, nAxis=defaultNamedNotOptArg, bIsAriesEPLSelected=defaultNamedNotOptArg, nSeriesSel=defaultNamedNotOptArg, nFrameSel=defaultNamedNotOptArg
			, nStackSel=defaultNamedNotOptArg, nWindingSel=defaultNamedNotOptArg, nFeedbackSel=defaultNamedNotOptArg, nCustomPartNumberSel=defaultNamedNotOptArg, nBaseSeriesSel=defaultNamedNotOptArg
			, strUserDefinedPartNumber=defaultNamedNotOptArg, nCustomWindingSel=defaultNamedNotOptArg, nCoolingSel=defaultNamedNotOptArg, nHeatSink=defaultNamedNotOptArg, bAdvancedSel=defaultNamedNotOptArg
			, strFullPartNumber=defaultNamedNotOptArg, strHeatSink=defaultNamedNotOptArg, strCustomWindingNumber=defaultNamedNotOptArg, bIsCustomResolution=defaultNamedNotOptArg):
		'EPL Drive Motor Settings'
		return self._oleobj_.InvokeTypes(155, LCID, 1, (24, 0), ((3, 1), (11, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (8, 1), (3, 1), (3, 1), (3, 1), (11, 1), (8, 1), (8, 1), (8, 1), (11, 1)),nAxis
			, bIsAriesEPLSelected, nSeriesSel, nFrameSel, nStackSel, nWindingSel
			, nFeedbackSel, nCustomPartNumberSel, nBaseSeriesSel, strUserDefinedPartNumber, nCustomWindingSel
			, nCoolingSel, nHeatSink, bAdvancedSel, strFullPartNumber, strHeatSink
			, strCustomWindingNumber, bIsCustomResolution)

	def PutEPLNodeData(self, nAxis=defaultNamedNotOptArg, nNodeID=defaultNamedNotOptArg, nMultiplexedCycleNumber=defaultNamedNotOptArg, nDriveMode=defaultNamedNotOptArg
			, nTCPIPPortNumber=defaultNamedNotOptArg, nReserved1=defaultNamedNotOptArg, nReserved2=defaultNamedNotOptArg):
		'EPL Settings'
		return self._oleobj_.InvokeTypes(153, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)),nAxis
			, nNodeID, nMultiplexedCycleNumber, nDriveMode, nTCPIPPortNumber, nReserved1
			, nReserved2)

	def PutEPLPeriod(self, dEPLPeriod=defaultNamedNotOptArg):
		'EPL Period'
		return self._oleobj_.InvokeTypes(162, LCID, 1, (24, 0), ((4, 1),),dEPLPeriod
			)

	def PutFaultOutputThermalInputData(self, nAxis=defaultNamedNotOptArg, bEnableFaultOnDriveDisable=defaultNamedNotOptArg, strOutputBrakeDelay=defaultNamedNotOptArg, bDisableMotorThermalSensor=defaultNamedNotOptArg
			, nMotorThermalSensorTypeSel=defaultNamedNotOptArg, nMotorThermalSensorConstructionSel=defaultNamedNotOptArg):
		'Fault Output Thermal Input Settings'
		return self._oleobj_.InvokeTypes(159, LCID, 1, (24, 0), ((3, 1), (11, 1), (8, 1), (11, 1), (3, 1), (3, 1)),nAxis
			, bEnableFaultOnDriveDisable, strOutputBrakeDelay, bDisableMotorThermalSensor, nMotorThermalSensorTypeSel, nMotorThermalSensorConstructionSel
			)

	def PutSetupHW(self, nCard=defaultNamedNotOptArg, nEncoder=defaultNamedNotOptArg, nServo1=defaultNamedNotOptArg, nStepper1=defaultNamedNotOptArg
			, nServo2=defaultNamedNotOptArg, nStepper2=defaultNamedNotOptArg, nAnalog=defaultNamedNotOptArg, nAnalogMode=defaultNamedNotOptArg, nIOMode=defaultNamedNotOptArg
			, nExpandedIO=defaultNamedNotOptArg):
		'Hardware Setup'
		return self._oleobj_.InvokeTypes(107, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)),nCard
			, nEncoder, nServo1, nStepper1, nServo2, nStepper2
			, nAnalog, nAnalogMode, nIOMode, nExpandedIO)

	def PutSetupHWex(self, nEncoder=defaultNamedNotOptArg, nServo1=defaultNamedNotOptArg, nStepper1=defaultNamedNotOptArg, nServo2=defaultNamedNotOptArg
			, nStepper2=defaultNamedNotOptArg, nAnalog=defaultNamedNotOptArg, nAnalogMode=defaultNamedNotOptArg):
		'Hardware Setup Ex'
		return self._oleobj_.InvokeTypes(109, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)),nEncoder
			, nServo1, nStepper1, nServo2, nStepper2, nAnalog
			, nAnalogMode)

	def PutSetupProfile(self, nProfile=defaultNamedNotOptArg, fVecVel=defaultNamedNotOptArg, fVecAcc=defaultNamedNotOptArg, fRampSTP=defaultNamedNotOptArg
			, fRampDEC=defaultNamedNotOptArg, bSCurve=defaultNamedNotOptArg, bEstopHWLimit=defaultNamedNotOptArg, bEstopSWLimit=defaultNamedNotOptArg, nSysCfgType=defaultNamedNotOptArg
			, bstrSysPartNbr=defaultNamedNotOptArg):
		'Setup Motion Profiles'
		return self._oleobj_.InvokeTypes(119, LCID, 1, (24, 0), ((3, 1), (4, 1), (4, 1), (4, 1), (4, 1), (11, 1), (11, 1), (11, 1), (3, 1), (8, 1)),nProfile
			, fVecVel, fVecAcc, fRampSTP, fRampDEC, bSCurve
			, bEstopHWLimit, bEstopSWLimit, nSysCfgType, bstrSysPartNbr)

	def PutUserData(self, bstrBody=defaultNamedNotOptArg):
		'User Data'
		return self._oleobj_.InvokeTypes(145, LCID, 1, (24, 0), ((8, 1),),bstrBody
			)

	def SaveAriesConfig(self, bAries=defaultNamedNotOptArg, bstrFile=defaultNamedNotOptArg):
		'Save Aries Configuration'
		return self._oleobj_.InvokeTypes(149, LCID, 1, (24, 0), ((11, 1), (8, 1)),bAries
			, bstrFile)

	def SaveConfig(self, bController=defaultNamedNotOptArg, bstrPath=defaultNamedNotOptArg):
		'Save Configuration'
		return self._oleobj_.InvokeTypes(120, LCID, 1, (24, 0), ((11, 1), (8, 1)),bController
			, bstrPath)

	def SetWatchdog(self, nInterval=defaultNamedNotOptArg, nRetries=defaultNamedNotOptArg):
		'Setup Watchdog'
		return self._oleobj_.InvokeTypes(132, LCID, 1, (24, 0), ((3, 1), (3, 1)),nInterval
			, nRetries)

	def TestConnect(self):
		'Test ACR Connection'
		return self._oleobj_.InvokeTypes(129, LCID, 1, (11, 0), (),)

	def getLJRAT(self, nAxis=defaultNamedNotOptArg, nDriveType=defaultNamedNotOptArg):
		'Load to Rotary Inertia Ratio'
		return self._oleobj_.InvokeTypes(139, LCID, 1, (3, 0), ((3, 1), (3, 1)),nAxis
			, nDriveType)

	_prop_map_get_ = {
		"bComment": (7, 2, (11, 0), (), "bComment", None),
		"bFaultOnDisable": (57, 2, (11, 0), (), "bFaultOnDisable", None),
		"bFoldback": (40, 2, (11, 0), (), "bFoldback", None),
		"bInPosnOutput": (52, 2, (11, 0), (), "bInPosnOutput", None),
		"bInvertAnalogIn": (34, 2, (11, 0), (), "bInvertAnalogIn", None),
		"bIsConfigured": (88, 2, (11, 0), (), "bIsConfigured", None),
		"bIsDriveFaulted": (89, 2, (11, 0), (), "bIsDriveFaulted", None),
		"bIsHWDriveEnabled": (90, 2, (11, 0), (), "bIsHWDriveEnabled", None),
		"bMtrThermDisable": (51, 2, (11, 0), (), "bMtrThermDisable", None),
		"bOnConnectTest": (11, 2, (11, 0), (), "bOnConnectTest", None),
		"bstrAriesPartNbr": (86, 2, (8, 0), (), "bstrAriesPartNbr", None),
		"bstrIP": (4, 2, (8, 0), (), "bstrIP", None),
		"bstrPartNbr": (8, 2, (8, 0), (), "bstrPartNbr", None),
		"bstrUSBSerialNumber": (14, 2, (8, 0), (), "bstrUSBSerialNumber", None),
		"bstrVersion": (1, 2, (8, 0), (), "bstrVersion", None),
		"fCenterDeadband": (36, 2, (4, 0), (), "fCenterDeadband", None),
		"fEleCurrentDeRate": (17, 2, (4, 0), (), "fEleCurrentDeRate", None),
		"fEleCurrentPeakRate": (18, 2, (4, 0), (), "fEleCurrentPeakRate", None),
		"fEleCurrentRate": (16, 2, (4, 0), (), "fEleCurrentRate", None),
		"fEleInductance": (19, 2, (4, 0), (), "fEleInductance", None),
		"fEleInductanceFact": (20, 2, (4, 0), (), "fEleInductanceFact", None),
		"fEleKe": (31, 2, (4, 0), (), "fEleKe", None),
		"fElePitch": (29, 2, (4, 0), (), "fElePitch", None),
		"fEleWindResist": (22, 2, (4, 0), (), "fEleWindResist", None),
		"fGainDerivative": (70, 2, (4, 0), (), "fGainDerivative", None),
		"fGainIntegral": (69, 2, (4, 0), (), "fGainIntegral", None),
		"fGainProportional": (68, 2, (4, 0), (), "fGainProportional", None),
		"fGainVelFeedforward": (74, 2, (4, 0), (), "fGainVelFeedforward", None),
		"fGainVelocity": (71, 2, (4, 0), (), "fGainVelocity", None),
		"fIGain": (37, 2, (4, 0), (), "fIGain", None),
		"fILimit": (67, 2, (4, 0), (), "fILimit", None),
		"fLoadRatio": (28, 2, (4, 0), (), "fLoadRatio", None),
		"fMaxStartVolts": (60, 2, (4, 0), (), "fMaxStartVolts", None),
		"fMaxVelErr": (81, 2, (4, 0), (), "fMaxVelErr", None),
		"fMtrAmbTemp": (63, 2, (4, 0), (), "fMtrAmbTemp", None),
		"fMtrDamping": (25, 2, (4, 0), (), "fMtrDamping", None),
		"fMtrInertia": (26, 2, (4, 0), (), "fMtrInertia", None),
		"fMtrRatedSpd": (23, 2, (4, 0), (), "fMtrRatedSpd", None),
		"fMtrThermConst": (65, 2, (4, 0), (), "fMtrThermConst", None),
		"fMtrWindTempMax": (21, 2, (4, 0), (), "fMtrWindTempMax", None),
		"fMtrWindThermConst": (66, 2, (4, 0), (), "fMtrWindThermConst", None),
		"fMtrWindThermResist": (64, 2, (4, 0), (), "fMtrWindThermResist", None),
		"fNotch1Depth": (42, 2, (4, 0), (), "fNotch1Depth", None),
		"fNotch1Quality": (44, 2, (4, 0), (), "fNotch1Quality", None),
		"fNotch2Depth": (45, 2, (4, 0), (), "fNotch2Depth", None),
		"fNotch2Quality": (47, 2, (4, 0), (), "fNotch2Quality", None),
		"fPGain": (38, 2, (4, 0), (), "fPGain", None),
		"fPushLimit": (30, 2, (4, 0), (), "fPushLimit", None),
		"fPushScale": (39, 2, (4, 0), (), "fPushScale", None),
		"fVGainIntegral": (79, 2, (4, 0), (), "fVGainIntegral", None),
		"fVGainProportional": (78, 2, (4, 0), (), "fVGainProportional", None),
		"fVelLimit": (56, 2, (4, 0), (), "fVelLimit", None),
		"fVelScale": (80, 2, (4, 0), (), "fVelScale", None),
		"isOffline": (6, 2, (11, 0), (), "isOffline", None),
		"nAutoCurr": (32, 2, (3, 0), (), "nAutoCurr", None),
		"nAutoCurrBandwidth": (33, 2, (3, 0), (), "nAutoCurrBandwidth", None),
		"nBPS": (3, 2, (3, 0), (), "nBPS", None),
		"nBus": (5, 2, (3, 0), (), "nBus", None),
		"nCard": (12, 2, (3, 0), (), "nCard", None),
		"nCmdDirection": (35, 2, (3, 0), (), "nCmdDirection", None),
		"nCommutationType": (58, 2, (3, 0), (), "nCommutationType", None),
		"nDMODE": (41, 2, (3, 0), (), "nDMODE", None),
		"nDimDef": (10, 2, (3, 0), (), "nDimDef", None),
		"nDimP": (9, 2, (3, 0), (), "nDimP", None),
		"nEncoderOffset": (84, 2, (3, 0), (), "nEncoderOffset", None),
		"nEncoderPolarity": (82, 2, (3, 0), (), "nEncoderPolarity", None),
		"nFbkPackage": (59, 2, (3, 0), (), "nFbkPackage", None),
		"nFbkResolution": (15, 2, (3, 0), (), "nFbkResolution", None),
		"nFirmwareVer": (13, 2, (3, 0), (), "nFirmwareVer", None),
		"nGainIntegralLimit": (73, 2, (3, 0), (), "nGainIntegralLimit", None),
		"nHallSensorDir": (85, 2, (3, 0), (), "nHallSensorDir", None),
		"nHallSensorInv": (83, 2, (3, 0), (), "nHallSensorInv", None),
		"nInPosnDeadBand": (54, 2, (3, 0), (), "nInPosnDeadBand", None),
		"nInPosnTimeout": (55, 2, (3, 0), (), "nInPosnTimeout", None),
		"nMaxPosnErr": (75, 2, (3, 0), (), "nMaxPosnErr", None),
		"nMtrHeatSink": (27, 2, (3, 0), (), "nMtrHeatSink", None),
		"nMtrPackage": (87, 2, (3, 0), (), "nMtrPackage", None),
		"nMtrPolePair": (24, 2, (3, 0), (), "nMtrPolePair", None),
		"nMtrThermType": (62, 2, (3, 0), (), "nMtrThermType", None),
		"nMtrWindingNbr": (61, 2, (3, 0), (), "nMtrWindingNbr", None),
		"nNotch1Hz": (43, 2, (3, 0), (), "nNotch1Hz", None),
		"nNotch2Hz": (46, 2, (3, 0), (), "nNotch2Hz", None),
		"nNotchLagHz": (49, 2, (3, 0), (), "nNotchLagHz", None),
		"nNotchLeadHz": (48, 2, (3, 0), (), "nNotchLeadHz", None),
		"nOutBkDelay": (53, 2, (3, 0), (), "nOutBkDelay", None),
		"nPWMSwitching": (50, 2, (3, 0), (), "nPWMSwitching", None),
		"nPort": (2, 2, (3, 0), (), "nPort", None),
		"nPosnScale": (76, 2, (3, 0), (), "nPosnScale", None),
		"nStepRes": (77, 2, (3, 0), (), "nStepRes", None),
		"nVGainIntegralLimit": (72, 2, (3, 0), (), "nVGainIntegralLimit", None),
	}
	_prop_map_put_ = {
		"bComment": ((7, LCID, 4, 0),()),
		"bFaultOnDisable": ((57, LCID, 4, 0),()),
		"bFoldback": ((40, LCID, 4, 0),()),
		"bInPosnOutput": ((52, LCID, 4, 0),()),
		"bInvertAnalogIn": ((34, LCID, 4, 0),()),
		"bMtrThermDisable": ((51, LCID, 4, 0),()),
		"bOnConnectTest": ((11, LCID, 4, 0),()),
		"bstrAriesPartNbr": ((86, LCID, 4, 0),()),
		"bstrIP": ((4, LCID, 4, 0),()),
		"bstrPartNbr": ((8, LCID, 4, 0),()),
		"bstrUSBSerialNumber": ((14, LCID, 4, 0),()),
		"fCenterDeadband": ((36, LCID, 4, 0),()),
		"fEleCurrentDeRate": ((17, LCID, 4, 0),()),
		"fEleCurrentPeakRate": ((18, LCID, 4, 0),()),
		"fEleCurrentRate": ((16, LCID, 4, 0),()),
		"fEleInductance": ((19, LCID, 4, 0),()),
		"fEleInductanceFact": ((20, LCID, 4, 0),()),
		"fEleKe": ((31, LCID, 4, 0),()),
		"fElePitch": ((29, LCID, 4, 0),()),
		"fEleWindResist": ((22, LCID, 4, 0),()),
		"fGainDerivative": ((70, LCID, 4, 0),()),
		"fGainIntegral": ((69, LCID, 4, 0),()),
		"fGainProportional": ((68, LCID, 4, 0),()),
		"fGainVelFeedforward": ((74, LCID, 4, 0),()),
		"fGainVelocity": ((71, LCID, 4, 0),()),
		"fIGain": ((37, LCID, 4, 0),()),
		"fILimit": ((67, LCID, 4, 0),()),
		"fLoadRatio": ((28, LCID, 4, 0),()),
		"fMaxStartVolts": ((60, LCID, 4, 0),()),
		"fMaxVelErr": ((81, LCID, 4, 0),()),
		"fMtrAmbTemp": ((63, LCID, 4, 0),()),
		"fMtrDamping": ((25, LCID, 4, 0),()),
		"fMtrInertia": ((26, LCID, 4, 0),()),
		"fMtrRatedSpd": ((23, LCID, 4, 0),()),
		"fMtrThermConst": ((65, LCID, 4, 0),()),
		"fMtrWindTempMax": ((21, LCID, 4, 0),()),
		"fMtrWindThermConst": ((66, LCID, 4, 0),()),
		"fMtrWindThermResist": ((64, LCID, 4, 0),()),
		"fNotch1Depth": ((42, LCID, 4, 0),()),
		"fNotch1Quality": ((44, LCID, 4, 0),()),
		"fNotch2Depth": ((45, LCID, 4, 0),()),
		"fNotch2Quality": ((47, LCID, 4, 0),()),
		"fPGain": ((38, LCID, 4, 0),()),
		"fPushLimit": ((30, LCID, 4, 0),()),
		"fPushScale": ((39, LCID, 4, 0),()),
		"fVGainIntegral": ((79, LCID, 4, 0),()),
		"fVGainProportional": ((78, LCID, 4, 0),()),
		"fVelLimit": ((56, LCID, 4, 0),()),
		"fVelScale": ((80, LCID, 4, 0),()),
		"nAutoCurr": ((32, LCID, 4, 0),()),
		"nAutoCurrBandwidth": ((33, LCID, 4, 0),()),
		"nBPS": ((3, LCID, 4, 0),()),
		"nBus": ((5, LCID, 4, 0),()),
		"nCmdDirection": ((35, LCID, 4, 0),()),
		"nCommutationType": ((58, LCID, 4, 0),()),
		"nDMODE": ((41, LCID, 4, 0),()),
		"nDimDef": ((10, LCID, 4, 0),()),
		"nDimP": ((9, LCID, 4, 0),()),
		"nEncoderOffset": ((84, LCID, 4, 0),()),
		"nEncoderPolarity": ((82, LCID, 4, 0),()),
		"nFbkPackage": ((59, LCID, 4, 0),()),
		"nFbkResolution": ((15, LCID, 4, 0),()),
		"nFirmwareVer": ((13, LCID, 4, 0),()),
		"nGainIntegralLimit": ((73, LCID, 4, 0),()),
		"nHallSensorDir": ((85, LCID, 4, 0),()),
		"nHallSensorInv": ((83, LCID, 4, 0),()),
		"nInPosnDeadBand": ((54, LCID, 4, 0),()),
		"nInPosnTimeout": ((55, LCID, 4, 0),()),
		"nMaxPosnErr": ((75, LCID, 4, 0),()),
		"nMtrHeatSink": ((27, LCID, 4, 0),()),
		"nMtrPackage": ((87, LCID, 4, 0),()),
		"nMtrPolePair": ((24, LCID, 4, 0),()),
		"nMtrThermType": ((62, LCID, 4, 0),()),
		"nMtrWindingNbr": ((61, LCID, 4, 0),()),
		"nNotch1Hz": ((43, LCID, 4, 0),()),
		"nNotch2Hz": ((46, LCID, 4, 0),()),
		"nNotchLagHz": ((49, LCID, 4, 0),()),
		"nNotchLeadHz": ((48, LCID, 4, 0),()),
		"nOutBkDelay": ((53, LCID, 4, 0),()),
		"nPWMSwitching": ((50, LCID, 4, 0),()),
		"nPort": ((2, LCID, 4, 0),()),
		"nPosnScale": ((76, LCID, 4, 0),()),
		"nStepRes": ((77, LCID, 4, 0),()),
		"nVGainIntegralLimit": ((72, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IControl(DispatchBaseClass):
	'IControl Interface'
	CLSID = IID('{57DA70AA-3B42-4345-A3A4-C19756A5056A}')
	coclass_clsid = IID('{B1E87CFE-70A7-444D-9528-321F6928D4B4}')

	def Arc(self, nMask=defaultNamedNotOptArg, targets=defaultNamedNotOptArg):
		'Perform an Arc Move'
		return self._oleobj_.InvokeTypes(106, LCID, 1, (24, 0), ((3, 1), (12, 1)),nMask
			, targets)

	def Connect(self, nTransport=defaultNamedNotOptArg, nIndex=defaultNamedNotOptArg):
		'Connect'
		return self._oleobj_.InvokeTypes(100, LCID, 1, (24, 0), ((3, 1), (3, 1)),nTransport
			, nIndex)

	def Disconnect(self):
		'Connect Offline'
		return self._oleobj_.InvokeTypes(99, LCID, 1, (24, 0), (),)

	def GetMoveCounter(self, nCounter=pythoncom.Missing, nIncrement=pythoncom.Missing):
		'Get Move Counter'
		return self._ApplyTypes_(112, 1, (24, 0), ((16387, 2), (16387, 2)), u'GetMoveCounter', None,nCounter
			, nIncrement)

	def GetPerformance(self):
		'Get Performance Data'
		return self._ApplyTypes_(120, 1, (12, 0), (), u'GetPerformance', None,)

	def InitPerformance(self):
		'Initialize Performance Data'
		return self._oleobj_.InvokeTypes(119, LCID, 1, (24, 0), (),)

	def Move(self, nMask=defaultNamedNotOptArg, targets=defaultNamedNotOptArg):
		'Perform a Move '
		return self._oleobj_.InvokeTypes(105, LCID, 1, (24, 0), ((3, 1), (12, 1)),nMask
			, targets)

	def MoveBatch(self, nType=defaultNamedNotOptArg, moves=defaultNamedNotOptArg):
		'Send Moves in Batch'
		return self._oleobj_.InvokeTypes(121, LCID, 1, (24, 0), ((3, 1), (12, 1)),nType
			, moves)

	def SendRES(self, nMask=defaultNamedNotOptArg):
		'Send a RES cmd'
		return self._oleobj_.InvokeTypes(109, LCID, 1, (24, 0), ((3, 1),),nMask
			)

	def SetACRMemory(self, nType=defaultNamedNotOptArg, nAddress=defaultNamedNotOptArg, values=defaultNamedNotOptArg):
		'Set ACR Memory'
		return self._oleobj_.InvokeTypes(114, LCID, 1, (24, 0), ((3, 1), (3, 1), (12, 1)),nType
			, nAddress, values)

	def SetACRMemoryMask(self, nAddress=defaultNamedNotOptArg, nNAND=defaultNamedNotOptArg, nOR=defaultNamedNotOptArg):
		'Set ACR Memory Mask'
		return self._oleobj_.InvokeTypes(115, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),nAddress
			, nNAND, nOR)

	def SetFOV(self, nMask=defaultNamedNotOptArg, fValue=defaultNamedNotOptArg):
		'Immediate FOV'
		return self._oleobj_.InvokeTypes(117, LCID, 1, (24, 0), ((3, 1), (4, 1)),nMask
			, fValue)

	def SetFlag(self, nBit=defaultNamedNotOptArg, bValue=defaultNamedNotOptArg, bFast=defaultNamedNotOptArg):
		'Set or Clear Flag'
		return self._oleobj_.InvokeTypes(101, LCID, 1, (24, 0), ((3, 1), (11, 1), (11, 1)),nBit
			, bValue, bFast)

	def SetGlobal(self, nCard=defaultNamedNotOptArg, nGlobal=defaultNamedNotOptArg, dValue=defaultNamedNotOptArg, bFast=defaultNamedNotOptArg):
		'Global Parameter Assignment'
		return self._oleobj_.InvokeTypes(104, LCID, 1, (24, 0), ((3, 1), (3, 1), (5, 1), (11, 1)),nCard
			, nGlobal, dValue, bFast)

	def SetMoveCounter(self, nCounter=defaultNamedNotOptArg, nIncrement=defaultNamedNotOptArg):
		'Set Move Counter'
		return self._oleobj_.InvokeTypes(113, LCID, 1, (24, 0), ((3, 1), (3, 1)),nCounter
			, nIncrement)

	def SetParmFloat(self, nPparm=defaultNamedNotOptArg, fValue=defaultNamedNotOptArg, bFast=defaultNamedNotOptArg):
		'p-Parameter Assignment Float'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((3, 1), (4, 1), (11, 1)),nPparm
			, fValue, bFast)

	def SetParmLong(self, nPparm=defaultNamedNotOptArg, nValue=defaultNamedNotOptArg, bFast=defaultNamedNotOptArg):
		'p-Parameter Assignment Long'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), ((3, 1), (3, 1), (11, 1)),nPparm
			, nValue, bFast)

	def SetParmLongMask(self, nPparm=defaultNamedNotOptArg, nNAND=defaultNamedNotOptArg, nOR=defaultNamedNotOptArg):
		'p-Parameter Mask Long'
		return self._oleobj_.InvokeTypes(116, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),nPparm
			, nNAND, nOR)

	def SetROV(self, nMask=defaultNamedNotOptArg, fValue=defaultNamedNotOptArg):
		'Immediate ROV'
		return self._oleobj_.InvokeTypes(118, LCID, 1, (24, 0), ((3, 1), (4, 1)),nMask
			, fValue)

	def SetWatchdog(self, nInterval=defaultNamedNotOptArg, nRetries=defaultNamedNotOptArg):
		'Setup Watchdog'
		return self._oleobj_.InvokeTypes(111, LCID, 1, (24, 0), ((3, 1), (3, 1)),nInterval
			, nRetries)

	def Stop(self, bDecel=defaultNamedNotOptArg):
		'Stop Commanded Motion'
		return self._oleobj_.InvokeTypes(108, LCID, 1, (24, 0), ((11, 1),),bDecel
			)

	def TestConnect(self):
		'Test ACR Connection'
		return self._oleobj_.InvokeTypes(110, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"bArcAbsolute": (15, 2, (11, 0), (), "bArcAbsolute", None),
		"bArcCCW": (16, 2, (11, 0), (), "bArcCCW", None),
		"bMoveAbsolute": (12, 2, (11, 0), (), "bMoveAbsolute", None),
		"bOnConnectTest": (17, 2, (11, 0), (), "bOnConnectTest", None),
		"bstrIP": (4, 2, (8, 0), (), "bstrIP", None),
		"bstrUSBSerialNumber": (19, 2, (8, 0), (), "bstrUSBSerialNumber", None),
		"bstrVersion": (1, 2, (8, 0), (), "bstrVersion", None),
		"fMoveACC": (10, 2, (4, 0), (), "fMoveACC", None),
		"fMoveFVEL": (9, 2, (4, 0), (), "fMoveFVEL", None),
		"fMoveVEL": (8, 2, (4, 0), (), "fMoveVEL", None),
		"isOffline": (6, 2, (11, 0), (), "isOffline", None),
		"nArcMode": (14, 2, (3, 0), (), "nArcMode", None),
		"nBPS": (3, 2, (3, 0), (), "nBPS", None),
		"nBus": (5, 2, (3, 0), (), "nBus", None),
		"nCard": (18, 2, (3, 0), (), "nCard", None),
		"nMoveCounter": (13, 2, (3, 0), (), "nMoveCounter", None),
		"nMoveMode": (11, 2, (3, 0), (), "nMoveMode", None),
		"nMoveProfile": (7, 2, (3, 0), (), "nMoveProfile", None),
		"nPort": (2, 2, (3, 0), (), "nPort", None),
	}
	_prop_map_put_ = {
		"bArcAbsolute": ((15, LCID, 4, 0),()),
		"bArcCCW": ((16, LCID, 4, 0),()),
		"bMoveAbsolute": ((12, LCID, 4, 0),()),
		"bOnConnectTest": ((17, LCID, 4, 0),()),
		"bstrIP": ((4, LCID, 4, 0),()),
		"bstrUSBSerialNumber": ((19, LCID, 4, 0),()),
		"fMoveACC": ((10, LCID, 4, 0),()),
		"fMoveFVEL": ((9, LCID, 4, 0),()),
		"fMoveVEL": ((8, LCID, 4, 0),()),
		"nArcMode": ((14, LCID, 4, 0),()),
		"nBPS": ((3, LCID, 4, 0),()),
		"nBus": ((5, LCID, 4, 0),()),
		"nMoveCounter": ((13, LCID, 4, 0),()),
		"nMoveMode": ((11, LCID, 4, 0),()),
		"nMoveProfile": ((7, LCID, 4, 0),()),
		"nPort": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IStatus(DispatchBaseClass):
	'IStatus Interface'
	CLSID = IID('{D71EADD4-66CD-44B2-A666-9A8A6D2FFD24}')
	coclass_clsid = IID('{454FE70D-5DC2-4128-A2C8-89B6D98F67C2}')

	def AddACRCustom(self, bstrRequest=defaultNamedNotOptArg):
		'Add ACRCustom request'
		return self._oleobj_.InvokeTypes(105, LCID, 1, (3, 0), ((8, 1),),bstrRequest
			)

	def AddACRGroup(self, bstrRequest=defaultNamedNotOptArg):
		'Add ACRGroup request'
		return self._oleobj_.InvokeTypes(104, LCID, 1, (3, 0), ((8, 1),),bstrRequest
			)

	def AddACRGroupRaw(self, nType=defaultNamedNotOptArg, nCode=defaultNamedNotOptArg, nIndex=defaultNamedNotOptArg):
		'Add ACRGroup request Raw'
		return self._oleobj_.InvokeTypes(116, LCID, 1, (3, 0), ((3, 1), (3, 1), (3, 1)),nType
			, nCode, nIndex)

	def AddACRMemory(self, nType=defaultNamedNotOptArg, nAddress=defaultNamedNotOptArg, nCount=defaultNamedNotOptArg):
		'Add ACRMemory request'
		return self._oleobj_.InvokeTypes(106, LCID, 1, (3, 0), ((3, 1), (3, 1), (3, 1)),nType
			, nAddress, nCount)

	def Connect(self, nTransport=defaultNamedNotOptArg, nIndex=defaultNamedNotOptArg):
		'Connect'
		return self._oleobj_.InvokeTypes(100, LCID, 1, (24, 0), ((3, 1), (3, 1)),nTransport
			, nIndex)

	def DelStatus(self, nMsgid=defaultNamedNotOptArg):
		'Delete a Status request'
		return self._oleobj_.InvokeTypes(108, LCID, 1, (24, 0), ((3, 1),),nMsgid
			)

	def Disconnect(self):
		'Connect Offline'
		return self._oleobj_.InvokeTypes(99, LCID, 1, (24, 0), (),)

	def GetACRCustom(self, bstrRequest=defaultNamedNotOptArg):
		'Get ACR Custom Status'
		return self._ApplyTypes_(102, 1, (12, 0), ((8, 1),), u'GetACRCustom', None,bstrRequest
			)

	def GetACRGroup(self, bstrRequest=defaultNamedNotOptArg):
		'Get ACR Group Status'
		return self._ApplyTypes_(101, 1, (12, 0), ((8, 1),), u'GetACRGroup', None,bstrRequest
			)

	def GetACRGroupRaw(self, nType=defaultNamedNotOptArg, nCode=defaultNamedNotOptArg, nIndex=defaultNamedNotOptArg):
		'Get ACR Group Status Raw'
		return self._ApplyTypes_(115, 1, (12, 0), ((3, 1), (3, 1), (3, 1)), u'GetACRGroupRaw', None,nType
			, nCode, nIndex)

	def GetACRMemory(self, nType=defaultNamedNotOptArg, nAddress=defaultNamedNotOptArg, nCount=defaultNamedNotOptArg):
		'Direct ACR Memory Access'
		return self._ApplyTypes_(103, 1, (12, 0), ((3, 1), (3, 1), (3, 1)), u'GetACRMemory', None,nType
			, nAddress, nCount)

	def GetLocalAddr(self, nProg=defaultNamedNotOptArg, nType=defaultNamedNotOptArg, nSize=pythoncom.Missing):
		'Get Local Var Address'
		return self._ApplyTypes_(109, 1, (3, 0), ((3, 1), (3, 1), (16387, 2)), u'GetLocalAddr', None,nProg
			, nType, nSize)

	def GetLocalArrayAddr(self, nProg=defaultNamedNotOptArg, nType=defaultNamedNotOptArg, nArray=defaultNamedNotOptArg, nSize=pythoncom.Missing):
		'Get Local Array Address'
		return self._ApplyTypes_(110, 1, (3, 0), ((3, 1), (3, 1), (3, 1), (16387, 2)), u'GetLocalArrayAddr', None,nProg
			, nType, nArray, nSize)

	def GetParmAddr(self, nParameter=defaultNamedNotOptArg):
		'Get pParameter Address'
		return self._oleobj_.InvokeTypes(118, LCID, 1, (3, 0), ((3, 1),),nParameter
			)

	def GetParmInfo(self, nParameter=defaultNamedNotOptArg, nType=pythoncom.Missing, nCode=pythoncom.Missing, nIndex=pythoncom.Missing
			, bstrCatagory=pythoncom.Missing, bstrDesc=pythoncom.Missing):
		'Get Parameter Info'
		return self._ApplyTypes_(113, 1, (11, 0), ((3, 1), (16387, 2), (16387, 2), (16387, 2), (16392, 2), (16392, 2)), u'GetParmInfo', None,nParameter
			, nType, nCode, nIndex, bstrCatagory, bstrDesc
			)

	def GetParmType(self, nParameter=defaultNamedNotOptArg):
		'Get Parameter Type'
		return self._oleobj_.InvokeTypes(117, LCID, 1, (3, 0), ((3, 1),),nParameter
			)

	def GetStatus(self, nMsgid=defaultNamedNotOptArg):
		'Get Status Information'
		return self._ApplyTypes_(107, 1, (12, 0), ((3, 1),), u'GetStatus', None,nMsgid
			)

	def IsFlagSet(self, nFlagGrp=defaultNamedNotOptArg, nFlagNdx=defaultNamedNotOptArg):
		'is Flag Set'
		return self._oleobj_.InvokeTypes(111, LCID, 1, (11, 0), ((3, 1), (3, 1)),nFlagGrp
			, nFlagNdx)

	def SetWatchdog(self, nInterval=defaultNamedNotOptArg, nRetries=defaultNamedNotOptArg):
		'Setup Watchdog'
		return self._oleobj_.InvokeTypes(114, LCID, 1, (24, 0), ((3, 1), (3, 1)),nInterval
			, nRetries)

	def TestConnect(self):
		'Test ACR Connection'
		return self._oleobj_.InvokeTypes(112, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"bOnConnectTest": (8, 2, (11, 0), (), "bOnConnectTest", None),
		"bstrIP": (4, 2, (8, 0), (), "bstrIP", None),
		"bstrUSBSerialNumber": (10, 2, (8, 0), (), "bstrUSBSerialNumber", None),
		"bstrVersion": (1, 2, (8, 0), (), "bstrVersion", None),
		"isOffline": (6, 2, (11, 0), (), "isOffline", None),
		"nBPS": (3, 2, (3, 0), (), "nBPS", None),
		"nBus": (5, 2, (3, 0), (), "nBus", None),
		"nCard": (9, 2, (3, 0), (), "nCard", None),
		"nPort": (2, 2, (3, 0), (), "nPort", None),
		"nStatusWaitRate": (7, 2, (3, 0), (), "nStatusWaitRate", None),
	}
	_prop_map_put_ = {
		"bOnConnectTest": ((8, LCID, 4, 0),()),
		"bstrIP": ((4, LCID, 4, 0),()),
		"bstrUSBSerialNumber": ((10, LCID, 4, 0),()),
		"nBPS": ((3, LCID, 4, 0),()),
		"nBus": ((5, LCID, 4, 0),()),
		"nPort": ((2, LCID, 4, 0),()),
		"nStatusWaitRate": ((7, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITerminal(DispatchBaseClass):
	'ITerminal Interface'
	CLSID = IID('{2EE309A6-546F-4FA4-B9AE-F76D91AA0133}')
	coclass_clsid = IID('{E8393629-2EFE-428A-BF36-365A46940735}')

	def Connect(self, nTransport=defaultNamedNotOptArg, nIndex=defaultNamedNotOptArg):
		'Connect'
		return self._oleobj_.InvokeTypes(100, LCID, 1, (24, 0), ((3, 1), (3, 1)),nTransport
			, nIndex)

	def Disconnect(self):
		'Connect Offline'
		return self._oleobj_.InvokeTypes(99, LCID, 1, (24, 0), (),)

	def Read(self):
		'Read Data'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(101, LCID, 1, (8, 0), (),)

	def SetWatchdog(self, nInterval=defaultNamedNotOptArg, nRetries=defaultNamedNotOptArg):
		'Setup Watchdog'
		return self._oleobj_.InvokeTypes(104, LCID, 1, (24, 0), ((3, 1), (3, 1)),nInterval
			, nRetries)

	def TalkTo(self, nMode=defaultNamedNotOptArg, nIndex=defaultNamedNotOptArg):
		'Talk To Drive'
		return self._oleobj_.InvokeTypes(105, LCID, 1, (3, 0), ((3, 1), (3, 1)),nMode
			, nIndex)

	def TestConnect(self):
		'Test ACR Connection'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (11, 0), (),)

	def Write(self, send=defaultNamedNotOptArg):
		'Write Data'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((8, 1),),send
			)

	_prop_map_get_ = {
		"bOnConnectTest": (8, 2, (11, 0), (), "bOnConnectTest", None),
		"bstrIP": (4, 2, (8, 0), (), "bstrIP", None),
		"bstrUSBSerialNumber": (10, 2, (8, 0), (), "bstrUSBSerialNumber", None),
		"bstrVersion": (1, 2, (8, 0), (), "bstrVersion", None),
		"isOffline": (6, 2, (11, 0), (), "isOffline", None),
		"nBPS": (3, 2, (3, 0), (), "nBPS", None),
		"nBus": (5, 2, (3, 0), (), "nBus", None),
		"nCard": (9, 2, (3, 0), (), "nCard", None),
		"nDataWaitRate": (7, 2, (3, 0), (), "nDataWaitRate", None),
		"nPort": (2, 2, (3, 0), (), "nPort", None),
	}
	_prop_map_put_ = {
		"bOnConnectTest": ((8, LCID, 4, 0),()),
		"bstrIP": ((4, LCID, 4, 0),()),
		"bstrUSBSerialNumber": ((10, LCID, 4, 0),()),
		"nBPS": ((3, LCID, 4, 0),()),
		"nBus": ((5, LCID, 4, 0),()),
		"nDataWaitRate": ((7, LCID, 4, 0),()),
		"nPort": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IUtility(DispatchBaseClass):
	'IUtility Interface'
	CLSID = IID('{D49EC970-1B96-4514-BE5A-BFC0E5AFFC4B}')
	coclass_clsid = IID('{FB28DD27-1AC4-43B9-AFD7-8CA6003EEB7D}')

	def Connect(self, nTransport=defaultNamedNotOptArg, nIndex=defaultNamedNotOptArg):
		'Connect'
		return self._oleobj_.InvokeTypes(100, LCID, 1, (24, 0), ((3, 1), (3, 1)),nTransport
			, nIndex)

	def DeviceIoControl(self, dwloControlCode=defaultNamedNotOptArg, saBuffer=defaultNamedNotOptArg):
		'Device IO Control'
		return self._ApplyTypes_(108, 1, (3, 0), ((3, 1), (16387, 3)), u'DeviceIoControl', None,dwloControlCode
			, saBuffer)

	def DeviceIoControl2(self, dwloControlCode=defaultNamedNotOptArg, saBuffer=defaultNamedNotOptArg, saBuffer2=defaultNamedNotOptArg):
		'Device IO Control2'
		return self._ApplyTypes_(109, 1, (3, 0), ((3, 1), (16387, 3), (16387, 3)), u'DeviceIoControl2', None,dwloControlCode
			, saBuffer, saBuffer2)

	def Disconnect(self):
		'Connect Offline'
		return self._oleobj_.InvokeTypes(99, LCID, 1, (24, 0), (),)

	def DownloadAriesEPLOS(self, nDevice=defaultNamedNotOptArg, bAllEPLDrives=defaultNamedNotOptArg, nAxis=defaultNamedNotOptArg, bstrFile=defaultNamedNotOptArg):
		'Download Aries EPL OS'
		return self._oleobj_.InvokeTypes(112, LCID, 1, (24, 0), ((3, 1), (11, 1), (3, 1), (8, 1)),nDevice
			, bAllEPLDrives, nAxis, bstrFile)

	def DownloadEPL(self, nDevice=defaultNamedNotOptArg, bstrFile=defaultNamedNotOptArg):
		'Download EPL OS'
		return self._oleobj_.InvokeTypes(111, LCID, 1, (24, 0), ((3, 1), (8, 1)),nDevice
			, bstrFile)

	def DownloadFile(self, bstrPrg=defaultNamedNotOptArg, bstrFile=defaultNamedNotOptArg):
		'Download File'
		return self._oleobj_.InvokeTypes(105, LCID, 1, (24, 0), ((8, 1), (8, 1)),bstrPrg
			, bstrFile)

	def DownloadOS(self, nDevice=defaultNamedNotOptArg, bstrFile=defaultNamedNotOptArg):
		'Download OS'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((3, 1), (8, 1)),nDevice
			, bstrFile)

	def FindACR(self, nTransport=defaultNamedNotOptArg):
		'Find ACR Devices'
		return self._ApplyTypes_(101, 1, (12, 0), ((3, 1),), u'FindACR', None,nTransport
			)

	def GetStatusDL(self, nTotal=pythoncom.Missing, nBytes=pythoncom.Missing):
		'Download Status'
		return self._ApplyTypes_(103, 1, (3, 0), ((16387, 2), (16387, 2)), u'GetStatusDL', None,nTotal
			, nBytes)

	def GetStatusDLEx(self, nTotal=pythoncom.Missing, nBytes=pythoncom.Missing, bstrExtendedErrorMessage=pythoncom.Missing):
		'Download Status Ex'
		return self._ApplyTypes_(113, 1, (3, 0), ((16387, 2), (16387, 2), (16392, 2)), u'GetStatusDLEx', None,nTotal
			, nBytes, bstrExtendedErrorMessage)

	def SetWatchdog(self, nInterval=defaultNamedNotOptArg, nRetries=defaultNamedNotOptArg):
		'Setup Watchdog'
		return self._oleobj_.InvokeTypes(110, LCID, 1, (24, 0), ((3, 1), (3, 1)),nInterval
			, nRetries)

	def StopDownload(self):
		'Stop Download'
		return self._oleobj_.InvokeTypes(104, LCID, 1, (24, 0), (),)

	def TestConnect(self):
		'Test ACR Connection'
		return self._oleobj_.InvokeTypes(107, LCID, 1, (11, 0), (),)

	def UploadFile(self, bstrPrg=defaultNamedNotOptArg, bstrFile=defaultNamedNotOptArg):
		'Upload File'
		return self._oleobj_.InvokeTypes(106, LCID, 1, (24, 0), ((8, 1), (8, 1)),bstrPrg
			, bstrFile)

	_prop_map_get_ = {
		"bOnConnectTest": (7, 2, (11, 0), (), "bOnConnectTest", None),
		"bstrIP": (4, 2, (8, 0), (), "bstrIP", None),
		"bstrUSBSerialNumber": (9, 2, (8, 0), (), "bstrUSBSerialNumber", None),
		"bstrVersion": (1, 2, (8, 0), (), "bstrVersion", None),
		"isOffline": (6, 2, (11, 0), (), "isOffline", None),
		"nBPS": (3, 2, (3, 0), (), "nBPS", None),
		"nBus": (5, 2, (3, 0), (), "nBus", None),
		"nCard": (8, 2, (3, 0), (), "nCard", None),
		"nPort": (2, 2, (3, 0), (), "nPort", None),
	}
	_prop_map_put_ = {
		"bOnConnectTest": ((7, LCID, 4, 0),()),
		"bstrIP": ((4, LCID, 4, 0),()),
		"bstrUSBSerialNumber": ((9, LCID, 4, 0),()),
		"nBPS": ((3, LCID, 4, 0),()),
		"nBus": ((5, LCID, 4, 0),()),
		"nPort": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _IStatusEvents:
	'_IStatusEvents Interface'
	CLSID = CLSID_Sink = IID('{548F6282-AEE7-4AFA-B1F6-8C85389DD697}')
	coclass_clsid = IID('{454FE70D-5DC2-4128-A2C8-89B6D98F67C2}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        3 : "OnWatchdogReconnect",
		        2 : "OnWatchdogTimeout",
		        1 : "OnStatusWaiting",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnWatchdogReconnect(self):
#		'Watchdog Reconnect'
#	def OnWatchdogTimeout(self):
#		'Watchdog Timeout'
#	def OnStatusWaiting(self, msgID=defaultNamedNotOptArg, error=defaultNamedNotOptArg):
#		'Status Waiting'


class _ITerminalEvents:
	'_ITerminalEvents Interface'
	CLSID = CLSID_Sink = IID('{A1C9E9E2-49BB-40A8-8A9B-301051D224F2}')
	coclass_clsid = IID('{E8393629-2EFE-428A-BF36-365A46940735}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnDataWaiting",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnDataWaiting(self):
#		'Data Waiting to be Read'


from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'BoxBridge.Config.1'
class Config(CoClassBaseClass): # A CoClass
	# Config Class
	CLSID = IID('{36682CAC-F0A6-45B3-AD99-A1A6F8A5B05F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IConfig,
	]
	default_interface = IConfig

# This CoClass is known by the name 'BoxBridge.Control.1'
class Control(CoClassBaseClass): # A CoClass
	# Control Class
	CLSID = IID('{B1E87CFE-70A7-444D-9528-321F6928D4B4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IControl,
	]
	default_interface = IControl

# This CoClass is known by the name 'BoxBridge.Status.1'
class Status(CoClassBaseClass): # A CoClass
	# Status Class
	CLSID = IID('{454FE70D-5DC2-4128-A2C8-89B6D98F67C2}')
	coclass_sources = [
		_IStatusEvents,
	]
	default_source = _IStatusEvents
	coclass_interfaces = [
		IStatus,
	]
	default_interface = IStatus

# This CoClass is known by the name 'BoxBridge.Terminal.1'
class Terminal(CoClassBaseClass): # A CoClass
	# Terminal Class
	CLSID = IID('{E8393629-2EFE-428A-BF36-365A46940735}')
	coclass_sources = [
		_ITerminalEvents,
	]
	default_source = _ITerminalEvents
	coclass_interfaces = [
		ITerminal,
	]
	default_interface = ITerminal

# This CoClass is known by the name 'BoxBridge.Utility.1'
class Utility(CoClassBaseClass): # A CoClass
	# Utility Class
	CLSID = IID('{FB28DD27-1AC4-43B9-AFD7-8CA6003EEB7D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IUtility,
	]
	default_interface = IUtility

IConfig_vtables_dispatch_ = 1
IConfig_vtables_ = [
	(( u'bstrVersion' , u'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'nPort' , u'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'nPort' , u'pVal' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'nBPS' , u'pVal' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'nBPS' , u'pVal' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'bstrIP' , u'pVal' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'bstrIP' , u'pVal' , ), 4, (4, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'nBus' , u'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'nBus' , u'pVal' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'isOffline' , u'pVal' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'bComment' , u'pVal' , ), 7, (7, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'bComment' , u'pVal' , ), 7, (7, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'bstrPartNbr' , u'pVal' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'bstrPartNbr' , u'pVal' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'nDimP' , u'pVal' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'nDimP' , u'pVal' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'nDimDef' , u'pVal' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'nDimDef' , u'pVal' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'bOnConnectTest' , u'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'bOnConnectTest' , u'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'nCard' , u'pVal' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'nFirmwareVer' , u'pVal' , ), 13, (13, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'nFirmwareVer' , u'pVal' , ), 13, (13, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'bstrUSBSerialNumber' , u'pVal' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'bstrUSBSerialNumber' , u'pVal' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'nFbkResolution' , u'pVal' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'nFbkResolution' , u'pVal' , ), 15, (15, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'fEleCurrentRate' , u'pVal' , ), 16, (16, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'fEleCurrentRate' , u'pVal' , ), 16, (16, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'fEleCurrentDeRate' , u'pVal' , ), 17, (17, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'fEleCurrentDeRate' , u'pVal' , ), 17, (17, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'fEleCurrentPeakRate' , u'pVal' , ), 18, (18, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'fEleCurrentPeakRate' , u'pVal' , ), 18, (18, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'fEleInductance' , u'pVal' , ), 19, (19, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'fEleInductance' , u'pVal' , ), 19, (19, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'fEleInductanceFact' , u'pVal' , ), 20, (20, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'fEleInductanceFact' , u'pVal' , ), 20, (20, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( u'fMtrWindTempMax' , u'pVal' , ), 21, (21, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'fMtrWindTempMax' , u'pVal' , ), 21, (21, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( u'fEleWindResist' , u'pVal' , ), 22, (22, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'fEleWindResist' , u'pVal' , ), 22, (22, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( u'fMtrRatedSpd' , u'pVal' , ), 23, (23, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'fMtrRatedSpd' , u'pVal' , ), 23, (23, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
	(( u'nMtrPolePair' , u'pVal' , ), 24, (24, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( u'nMtrPolePair' , u'pVal' , ), 24, (24, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
	(( u'fMtrDamping' , u'pVal' , ), 25, (25, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( u'fMtrDamping' , u'pVal' , ), 25, (25, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 212 , (3, 0, None, None) , 0 , )),
	(( u'fMtrInertia' , u'pVal' , ), 26, (26, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( u'fMtrInertia' , u'pVal' , ), 26, (26, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 220 , (3, 0, None, None) , 0 , )),
	(( u'nMtrHeatSink' , u'pVal' , ), 27, (27, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( u'nMtrHeatSink' , u'pVal' , ), 27, (27, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 228 , (3, 0, None, None) , 0 , )),
	(( u'fLoadRatio' , u'pVal' , ), 28, (28, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( u'fLoadRatio' , u'pVal' , ), 28, (28, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 236 , (3, 0, None, None) , 0 , )),
	(( u'fElePitch' , u'pVal' , ), 29, (29, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( u'fElePitch' , u'pVal' , ), 29, (29, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 244 , (3, 0, None, None) , 0 , )),
	(( u'fPushLimit' , u'pVal' , ), 30, (30, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( u'fPushLimit' , u'pVal' , ), 30, (30, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 252 , (3, 0, None, None) , 0 , )),
	(( u'fEleKe' , u'pVal' , ), 31, (31, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( u'fEleKe' , u'pVal' , ), 31, (31, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 260 , (3, 0, None, None) , 0 , )),
	(( u'nAutoCurr' , u'pVal' , ), 32, (32, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( u'nAutoCurr' , u'pVal' , ), 32, (32, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 268 , (3, 0, None, None) , 0 , )),
	(( u'nAutoCurrBandwidth' , u'pVal' , ), 33, (33, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( u'nAutoCurrBandwidth' , u'pVal' , ), 33, (33, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 276 , (3, 0, None, None) , 0 , )),
	(( u'bInvertAnalogIn' , u'pVal' , ), 34, (34, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( u'bInvertAnalogIn' , u'pVal' , ), 34, (34, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 284 , (3, 0, None, None) , 0 , )),
	(( u'nCmdDirection' , u'pVal' , ), 35, (35, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( u'nCmdDirection' , u'pVal' , ), 35, (35, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 292 , (3, 0, None, None) , 0 , )),
	(( u'fCenterDeadband' , u'pVal' , ), 36, (36, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( u'fCenterDeadband' , u'pVal' , ), 36, (36, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 300 , (3, 0, None, None) , 0 , )),
	(( u'fIGain' , u'pVal' , ), 37, (37, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( u'fIGain' , u'pVal' , ), 37, (37, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 308 , (3, 0, None, None) , 0 , )),
	(( u'fPGain' , u'pVal' , ), 38, (38, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( u'fPGain' , u'pVal' , ), 38, (38, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 316 , (3, 0, None, None) , 0 , )),
	(( u'fPushScale' , u'pVal' , ), 39, (39, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( u'fPushScale' , u'pVal' , ), 39, (39, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 324 , (3, 0, None, None) , 0 , )),
	(( u'bFoldback' , u'pVal' , ), 40, (40, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( u'bFoldback' , u'pVal' , ), 40, (40, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 332 , (3, 0, None, None) , 0 , )),
	(( u'nDMODE' , u'pVal' , ), 41, (41, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( u'nDMODE' , u'pVal' , ), 41, (41, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 340 , (3, 0, None, None) , 0 , )),
	(( u'fNotch1Depth' , u'pVal' , ), 42, (42, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( u'fNotch1Depth' , u'pVal' , ), 42, (42, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 348 , (3, 0, None, None) , 0 , )),
	(( u'nNotch1Hz' , u'pVal' , ), 43, (43, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( u'nNotch1Hz' , u'pVal' , ), 43, (43, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 356 , (3, 0, None, None) , 0 , )),
	(( u'fNotch1Quality' , u'pVal' , ), 44, (44, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( u'fNotch1Quality' , u'pVal' , ), 44, (44, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 364 , (3, 0, None, None) , 0 , )),
	(( u'fNotch2Depth' , u'pVal' , ), 45, (45, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( u'fNotch2Depth' , u'pVal' , ), 45, (45, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 372 , (3, 0, None, None) , 0 , )),
	(( u'nNotch2Hz' , u'pVal' , ), 46, (46, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( u'nNotch2Hz' , u'pVal' , ), 46, (46, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 380 , (3, 0, None, None) , 0 , )),
	(( u'fNotch2Quality' , u'pVal' , ), 47, (47, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( u'fNotch2Quality' , u'pVal' , ), 47, (47, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 388 , (3, 0, None, None) , 0 , )),
	(( u'nNotchLeadHz' , u'pVal' , ), 48, (48, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( u'nNotchLeadHz' , u'pVal' , ), 48, (48, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 396 , (3, 0, None, None) , 0 , )),
	(( u'nNotchLagHz' , u'pVal' , ), 49, (49, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( u'nNotchLagHz' , u'pVal' , ), 49, (49, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 404 , (3, 0, None, None) , 0 , )),
	(( u'nPWMSwitching' , u'pVal' , ), 50, (50, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( u'nPWMSwitching' , u'pVal' , ), 50, (50, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 412 , (3, 0, None, None) , 0 , )),
	(( u'bMtrThermDisable' , u'pVal' , ), 51, (51, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( u'bMtrThermDisable' , u'pVal' , ), 51, (51, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 420 , (3, 0, None, None) , 0 , )),
	(( u'bInPosnOutput' , u'pVal' , ), 52, (52, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( u'bInPosnOutput' , u'pVal' , ), 52, (52, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 428 , (3, 0, None, None) , 0 , )),
	(( u'nOutBkDelay' , u'pVal' , ), 53, (53, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( u'nOutBkDelay' , u'pVal' , ), 53, (53, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 436 , (3, 0, None, None) , 0 , )),
	(( u'nInPosnDeadBand' , u'pVal' , ), 54, (54, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( u'nInPosnDeadBand' , u'pVal' , ), 54, (54, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 444 , (3, 0, None, None) , 0 , )),
	(( u'nInPosnTimeout' , u'pVal' , ), 55, (55, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( u'nInPosnTimeout' , u'pVal' , ), 55, (55, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 452 , (3, 0, None, None) , 0 , )),
	(( u'fVelLimit' , u'pVal' , ), 56, (56, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( u'fVelLimit' , u'pVal' , ), 56, (56, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 460 , (3, 0, None, None) , 0 , )),
	(( u'bFaultOnDisable' , u'pVal' , ), 57, (57, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( u'bFaultOnDisable' , u'pVal' , ), 57, (57, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 468 , (3, 0, None, None) , 0 , )),
	(( u'nCommutationType' , u'pVal' , ), 58, (58, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( u'nCommutationType' , u'pVal' , ), 58, (58, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 476 , (3, 0, None, None) , 0 , )),
	(( u'nFbkPackage' , u'pVal' , ), 59, (59, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( u'nFbkPackage' , u'pVal' , ), 59, (59, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 484 , (3, 0, None, None) , 0 , )),
	(( u'fMaxStartVolts' , u'pVal' , ), 60, (60, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( u'fMaxStartVolts' , u'pVal' , ), 60, (60, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 492 , (3, 0, None, None) , 0 , )),
	(( u'nMtrWindingNbr' , u'pVal' , ), 61, (61, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( u'nMtrWindingNbr' , u'pVal' , ), 61, (61, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 500 , (3, 0, None, None) , 0 , )),
	(( u'nMtrThermType' , u'pVal' , ), 62, (62, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( u'nMtrThermType' , u'pVal' , ), 62, (62, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 508 , (3, 0, None, None) , 0 , )),
	(( u'fMtrAmbTemp' , u'pVal' , ), 63, (63, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( u'fMtrAmbTemp' , u'pVal' , ), 63, (63, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 516 , (3, 0, None, None) , 0 , )),
	(( u'fMtrWindThermResist' , u'pVal' , ), 64, (64, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( u'fMtrWindThermResist' , u'pVal' , ), 64, (64, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 524 , (3, 0, None, None) , 0 , )),
	(( u'fMtrThermConst' , u'pVal' , ), 65, (65, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( u'fMtrThermConst' , u'pVal' , ), 65, (65, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 532 , (3, 0, None, None) , 0 , )),
	(( u'fMtrWindThermConst' , u'pVal' , ), 66, (66, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( u'fMtrWindThermConst' , u'pVal' , ), 66, (66, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 540 , (3, 0, None, None) , 0 , )),
	(( u'fILimit' , u'pVal' , ), 67, (67, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( u'fILimit' , u'pVal' , ), 67, (67, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 548 , (3, 0, None, None) , 0 , )),
	(( u'fGainProportional' , u'pVal' , ), 68, (68, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( u'fGainProportional' , u'pVal' , ), 68, (68, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 556 , (3, 0, None, None) , 0 , )),
	(( u'fGainIntegral' , u'pVal' , ), 69, (69, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( u'fGainIntegral' , u'pVal' , ), 69, (69, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 564 , (3, 0, None, None) , 0 , )),
	(( u'fGainDerivative' , u'pVal' , ), 70, (70, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( u'fGainDerivative' , u'pVal' , ), 70, (70, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 572 , (3, 0, None, None) , 0 , )),
	(( u'fGainVelocity' , u'pVal' , ), 71, (71, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( u'fGainVelocity' , u'pVal' , ), 71, (71, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 580 , (3, 0, None, None) , 0 , )),
	(( u'nVGainIntegralLimit' , u'pVal' , ), 72, (72, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( u'nVGainIntegralLimit' , u'pVal' , ), 72, (72, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 588 , (3, 0, None, None) , 0 , )),
	(( u'nGainIntegralLimit' , u'pVal' , ), 73, (73, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( u'nGainIntegralLimit' , u'pVal' , ), 73, (73, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 596 , (3, 0, None, None) , 0 , )),
	(( u'fGainVelFeedforward' , u'pVal' , ), 74, (74, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( u'fGainVelFeedforward' , u'pVal' , ), 74, (74, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 604 , (3, 0, None, None) , 0 , )),
	(( u'nMaxPosnErr' , u'pVal' , ), 75, (75, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( u'nMaxPosnErr' , u'pVal' , ), 75, (75, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 612 , (3, 0, None, None) , 0 , )),
	(( u'nPosnScale' , u'pVal' , ), 76, (76, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( u'nPosnScale' , u'pVal' , ), 76, (76, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 620 , (3, 0, None, None) , 0 , )),
	(( u'nStepRes' , u'pVal' , ), 77, (77, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( u'nStepRes' , u'pVal' , ), 77, (77, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 628 , (3, 0, None, None) , 0 , )),
	(( u'fVGainProportional' , u'pVal' , ), 78, (78, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( u'fVGainProportional' , u'pVal' , ), 78, (78, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 636 , (3, 0, None, None) , 0 , )),
	(( u'fVGainIntegral' , u'pVal' , ), 79, (79, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( u'fVGainIntegral' , u'pVal' , ), 79, (79, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 644 , (3, 0, None, None) , 0 , )),
	(( u'fVelScale' , u'pVal' , ), 80, (80, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( u'fVelScale' , u'pVal' , ), 80, (80, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 652 , (3, 0, None, None) , 0 , )),
	(( u'fMaxVelErr' , u'pVal' , ), 81, (81, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( u'fMaxVelErr' , u'pVal' , ), 81, (81, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 660 , (3, 0, None, None) , 0 , )),
	(( u'nEncoderPolarity' , u'pVal' , ), 82, (82, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( u'nEncoderPolarity' , u'pVal' , ), 82, (82, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 668 , (3, 0, None, None) , 0 , )),
	(( u'nHallSensorInv' , u'pVal' , ), 83, (83, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( u'nHallSensorInv' , u'pVal' , ), 83, (83, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 676 , (3, 0, None, None) , 0 , )),
	(( u'nEncoderOffset' , u'pVal' , ), 84, (84, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( u'nEncoderOffset' , u'pVal' , ), 84, (84, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 684 , (3, 0, None, None) , 0 , )),
	(( u'nHallSensorDir' , u'pVal' , ), 85, (85, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( u'nHallSensorDir' , u'pVal' , ), 85, (85, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 692 , (3, 0, None, None) , 0 , )),
	(( u'bstrAriesPartNbr' , u'pVal' , ), 86, (86, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( u'bstrAriesPartNbr' , u'pVal' , ), 86, (86, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 700 , (3, 0, None, None) , 0 , )),
	(( u'nMtrPackage' , u'pVal' , ), 87, (87, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( u'nMtrPackage' , u'pVal' , ), 87, (87, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 708 , (3, 0, None, None) , 0 , )),
	(( u'bIsConfigured' , u'pVal' , ), 88, (88, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( u'bIsDriveFaulted' , u'pVal' , ), 89, (89, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 716 , (3, 0, None, None) , 0 , )),
	(( u'bIsHWDriveEnabled' , u'pVal' , ), 90, (90, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( u'Disconnect' , ), 99, (99, (), [ ], 1 , 1 , 4 , 0 , 724 , (3, 0, None, None) , 0 , )),
	(( u'GetDimProg' , u'nIndex' , u'nMemory' , ), 100, (100, (), [ (3, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( u'GetDimProgDefault' , u'nIndex' , u'nMemory' , ), 101, (101, (), [ (3, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 732 , (3, 0, None, None) , 0 , )),
	(( u'PutDimProgDefault' , u'nIndex' , u'nMemory' , ), 102, (102, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( u'GetDimPLC' , u'nIndex' , u'nMemory' , ), 103, (103, (), [ (3, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 740 , (3, 0, None, None) , 0 , )),
	(( u'GetDimPLCDefault' , u'nIndex' , u'nMemory' , ), 104, (104, (), [ (3, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( u'PutDimPLCDefault' , u'nIndex' , u'nMemory' , ), 105, (105, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 748 , (3, 0, None, None) , 0 , )),
	(( u'GetSetupHW' , u'nCard' , u'nEncoder' , u'nServo1' , u'nStepper1' , 
			u'nServo2' , u'nStepper2' , u'nAnalog' , u'nAnalogMode' , u'nIOMode' , 
			u'nExpandedIO' , ), 106, (106, (), [ (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( u'PutSetupHW' , u'nCard' , u'nEncoder' , u'nServo1' , u'nStepper1' , 
			u'nServo2' , u'nStepper2' , u'nAnalog' , u'nAnalogMode' , u'nIOMode' , 
			u'nExpandedIO' , ), 107, (107, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 756 , (3, 0, None, None) , 0 , )),
	(( u'GetSetupHWex' , u'nEncoder' , u'nServo1' , u'nStepper1' , u'nServo2' , 
			u'nStepper2' , u'nAnalog' , u'nAnalogMode' , ), 108, (108, (), [ (16387, 2, None, None) , 
			(16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 760 , (3, 0, None, None) , 0 , )),
	(( u'PutSetupHWex' , u'nEncoder' , u'nServo1' , u'nStepper1' , u'nServo2' , 
			u'nStepper2' , u'nAnalog' , u'nAnalogMode' , ), 109, (109, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 764 , (3, 0, None, None) , 0 , )),
	(( u'GetAxisFeedback' , u'nAxis' , u'nPosnType' , u'nPosnIndex' , u'nPosnQuad' , 
			u'nPosnSrc' , u'nPosnPkg' , u'fPosnRes' , u'nPosSmper' , u'nNegSmper' , 
			u'nVelType' , u'nVelIndex' , u'nVelQuad' , u'nVelSrc' , u'nVelPkg' , 
			u'fVelRes' , ), 110, (110, (), [ (3, 1, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , 
			(16388, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , (16388, 2, None, None) , ], 1 , 1 , 4 , 0 , 768 , (3, 0, None, None) , 0 , )),
	(( u'PutAxisFeedback' , u'nAxis' , u'nPosnType' , u'nPosnIndex' , u'nPosnQuad' , 
			u'nPosnSrc' , u'nPosnPkg' , u'fPosnRes' , u'nPosSmper' , u'nNegSmper' , 
			u'nVelType' , u'nVelIndex' , u'nVelQuad' , u'nVelSrc' , u'nVelPkg' , 
			u'fVelRes' , ), 111, (111, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 772 , (3, 0, None, None) , 0 , )),
	(( u'GetAxisIO' , u'nAxis' , u'nHwPosLimit' , u'nHwPosLimitLevel' , u'nHwNegLimit' , 
			u'nHwNegLimitLevel' , u'nHwHomeLimit' , u'nHwHomeLevel' , u'nDriveFault' , u'nDriveFaultLevel' , 
			u'nDriveEnable' , u'nDriveEnableLevel' , u'nDriveReset' , u'nDriveResetLevel' , u'bOnKill' , 
			), 112, (112, (), [ (3, 1, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16395, 2, None, None) , ], 1 , 1 , 4 , 0 , 776 , (3, 0, None, None) , 0 , )),
	(( u'PutAxisIO' , u'nAxis' , u'nHwPosLimit' , u'nHwPosLimitLevel' , u'nHwNegLimit' , 
			u'nHwNegLimitLevel' , u'nHwHomeLimit' , u'nHwHomeLevel' , u'nDriveFault' , u'nDriveFaultLevel' , 
			u'nDriveEnable' , u'nDriveEnableLevel' , u'nDriveReset' , u'nDriveResetLevel' , u'bOnKill' , 
			), 113, (113, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 780 , (3, 0, None, None) , 0 , )),
	(( u'GetAxisLimits' , u'nAxis' , u'bHwPos' , u'bHwNeg' , u'fHwLimitStp' , 
			u'bHwHome' , u'bSwPos' , u'fSwPosValue' , u'bSwNeg' , u'fSwNegValue' , 
			u'fSwLimitStp' , u'fVelLimit' , ), 114, (114, (), [ (3, 1, None, None) , (16395, 2, None, None) , 
			(16395, 2, None, None) , (16388, 2, None, None) , (16395, 2, None, None) , (16395, 2, None, None) , (16388, 2, None, None) , 
			(16395, 2, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , ], 1 , 1 , 4 , 0 , 784 , (3, 0, None, None) , 0 , )),
	(( u'PutAxisLimits' , u'nAxis' , u'bHwPos' , u'bHwNeg' , u'fHwLimitStp' , 
			u'bHwHome' , u'bSwPos' , u'fSwPosValue' , u'bSwNeg' , u'fSwNegValue' , 
			u'fSwLimitStp' , u'fVelLimit' , ), 115, (115, (), [ (3, 1, None, None) , (11, 1, None, None) , 
			(11, 1, None, None) , (4, 1, None, None) , (11, 1, None, None) , (11, 1, None, None) , (4, 1, None, None) , 
			(11, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 788 , (3, 0, None, None) , 0 , )),
	(( u'GetAxisProfile' , u'nAxis' , u'nProfile' , u'bstrName' , ), 116, (116, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 792 , (3, 0, None, None) , 0 , )),
	(( u'PutAxisProfile' , u'nAxis' , u'nProfile' , u'bstrName' , ), 117, (117, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 796 , (3, 0, None, None) , 0 , )),
	(( u'GetSetupProfile' , u'nProfile' , u'fVecVel' , u'fVecAcc' , u'fRampSTP' , 
			u'fRampDEC' , u'bSCurve' , u'bEstopHWLimit' , u'bEstopSWLimit' , u'nSysCfgType' , 
			u'bstrSysPartNbr' , ), 118, (118, (), [ (3, 1, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , 
			(16388, 2, None, None) , (16388, 2, None, None) , (16395, 2, None, None) , (16395, 2, None, None) , (16395, 2, None, None) , 
			(16387, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 800 , (3, 0, None, None) , 0 , )),
	(( u'PutSetupProfile' , u'nProfile' , u'fVecVel' , u'fVecAcc' , u'fRampSTP' , 
			u'fRampDEC' , u'bSCurve' , u'bEstopHWLimit' , u'bEstopSWLimit' , u'nSysCfgType' , 
			u'bstrSysPartNbr' , ), 119, (119, (), [ (3, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (4, 1, None, None) , (11, 1, None, None) , (11, 1, None, None) , (11, 1, None, None) , 
			(3, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 804 , (3, 0, None, None) , 0 , )),
	(( u'SaveConfig' , u'bController' , u'bstrPath' , ), 120, (120, (), [ (11, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 808 , (3, 0, None, None) , 0 , )),
	(( u'LoadConfig' , u'bstrPath' , ), 121, (121, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 812 , (3, 0, None, None) , 0 , )),
	(( u'GetAxisScale' , u'nAxis' , u'nUnits' , u'bstrUnitsName' , u'nTrans' , 
			u'fTransFactor' , u'nReducer' , u'fRedFactor1' , u'fRedFactor2' , u'fRedFactor3' , 
			u'fRedFactor4' , u'fSclFactor' , u'fPPU' , u'nLoadOrder' , u'fLoadAmt' , 
			u'bstrPartNbr' , ), 122, (122, (), [ (3, 1, None, None) , (16387, 2, None, None) , (16392, 2, None, None) , 
			(16387, 2, None, None) , (16388, 2, None, None) , (16387, 2, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , 
			(16388, 2, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , (16389, 2, None, None) , (16387, 2, None, None) , 
			(16388, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 816 , (3, 0, None, None) , 0 , )),
	(( u'PutAxisScale' , u'nAxis' , u'nUnits' , u'bstrUnitsName' , u'nTrans' , 
			u'fTransFactor' , u'nReducer' , u'fRedFactor1' , u'fRedFactor2' , u'fRedFactor3' , 
			u'fRedFactor4' , u'fSclFactor' , u'fPPU' , u'nLoadOrder' , u'fLoadAmt' , 
			u'bstrPartNbr' , ), 123, (123, (), [ (3, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , 
			(3, 1, None, None) , (4, 1, None, None) , (3, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (5, 1, None, None) , (3, 1, None, None) , 
			(4, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 820 , (3, 0, None, None) , 0 , )),
	(( u'GetAxisSignal' , u'nAxis' , u'nSignalType' , u'nSignalIndex' , u'nStepMode' , 
			u'nDrive' , u'nDriveRes' , u'nMotor' , u'nMotorPkg' , u'nGearHead' , 
			), 124, (124, (), [ (3, 1, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 824 , (3, 0, None, None) , 0 , )),
	(( u'PutAxisSignal' , u'nAxis' , u'nSignalType' , u'nSignalIndex' , u'nStepMode' , 
			u'nDrive' , u'nDriveRes' , u'nMotor' , u'nMotorPkg' , u'nGearHead' , 
			), 125, (125, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 828 , (3, 0, None, None) , 0 , )),
	(( u'GetCANopen' , u'nMaster' , u'nBitRate' , u'nPeriod' , u'nNodes' , 
			), 126, (126, (), [ (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 832 , (3, 0, None, None) , 0 , )),
	(( u'PutCANopen' , u'nMaster' , u'nBitRate' , u'nPeriod' , u'nNodes' , 
			), 127, (127, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 836 , (3, 0, None, None) , 0 , )),
	(( u'Connect' , u'nTransport' , u'nIndex' , ), 128, (128, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 840 , (3, 0, None, None) , 0 , )),
	(( u'TestConnect' , u'pVal' , ), 129, (129, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 844 , (3, 0, None, None) , 0 , )),
	(( u'GetCANnode' , u'nNode' , u'nNodeID' , u'nDInput' , u'nDOutput' , 
			u'nAInput' , u'nAOutput' , u'nType' , u'nTimeBase' , u'nTimeDPoint' , 
			u'nTimeAPoint' , ), 130, (130, (), [ (3, 1, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 848 , (3, 0, None, None) , 0 , )),
	(( u'PutCANnode' , u'nNode' , u'nNodeID' , u'nDInput' , u'nDOutput' , 
			u'nAInput' , u'nAOutput' , u'nType' , u'nTimeBase' , u'nTimeDPoint' , 
			u'nTimeAPoint' , ), 131, (131, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 852 , (3, 0, None, None) , 0 , )),
	(( u'SetWatchdog' , u'nInterval' , u'nRetries' , ), 132, (132, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 856 , (3, 0, None, None) , 0 , )),
	(( u'GetAxisGains' , u'nAxis' , u'fPropGain' , u'fIntGain' , u'fIntLimit' , 
			u'fIntDelay' , u'fDerGain' , u'fDerWidth' , u'fFeedFVel' , u'fFeedFAcc' , 
			u'fTorqLimit' , u'fFBackVel' , ), 135, (135, (), [ (3, 1, None, None) , (16388, 2, None, None) , 
			(16388, 2, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , 
			(16388, 2, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , ], 1 , 1 , 4 , 0 , 860 , (3, 0, None, None) , 0 , )),
	(( u'PutAxisGains' , u'nAxis' , u'fPropGain' , u'fIntGain' , u'fIntLimit' , 
			u'fIntDelay' , u'fDerGain' , u'fDerWidth' , u'fFeedFVel' , u'fFeedFAcc' , 
			u'fTorqLimit' , u'fFBackVel' , ), 136, (136, (), [ (3, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 864 , (3, 0, None, None) , 0 , )),
	(( u'GetAxisJog' , u'nAxis' , u'fJogAcc' , u'fJogVel' , u'fJogDec' , 
			u'fJogJrk' , u'fJogPosLimit' , u'fJogNegLimit' , u'bJogEnableLimit' , u'bJogLockout' , 
			), 137, (137, (), [ (3, 1, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , 
			(16388, 2, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , (16395, 2, None, None) , (16395, 2, None, None) , ], 1 , 1 , 4 , 0 , 868 , (3, 0, None, None) , 0 , )),
	(( u'PutAxisJog' , u'nAxis' , u'fJogAcc' , u'fJogVel' , u'fJogDec' , 
			u'fJogJrk' , u'fJogPosLimit' , u'fJogNegLimit' , u'bJogEnableLimit' , u'bJogLockout' , 
			), 138, (138, (), [ (3, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (11, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 872 , (3, 0, None, None) , 0 , )),
	(( u'getLJRAT' , u'nAxis' , u'nDriveType' , u'pVal' , ), 139, (139, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 876 , (3, 0, None, None) , 0 , )),
	(( u'GetAxisHome' , u'nAxis' , u'fHomAcc' , u'fHomVel' , u'fHomDec' , 
			u'fHomJrk' , u'fHomFinV' , u'nHomBackup' , u'nHomFinDir' , u'nHomEdge' , 
			), 140, (140, (), [ (3, 1, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , 
			(16388, 2, None, None) , (16388, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 880 , (3, 0, None, None) , 0 , )),
	(( u'PutAxisHome' , u'nAxis' , u'fHomAcc' , u'fHomVel' , u'fHomDec' , 
			u'fHomJrk' , u'fHomFinV' , u'nHomBackup' , u'nHomFinDir' , u'nHomEdge' , 
			), 141, (141, (), [ (3, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , (4, 1, None, None) , 
			(4, 1, None, None) , (4, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 884 , (3, 0, None, None) , 0 , )),
	(( u'GetAxisSsiData' , u'nAxis' , u'nPosnClock' , u'nPosnDST' , u'nPosnWidth' , 
			u'nPosnLimit' , u'nVelClock' , u'nVelDST' , u'nVelWidth' , u'nVelLimit' , 
			), 142, (142, (), [ (3, 1, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 888 , (3, 0, None, None) , 0 , )),
	(( u'PutAxisSsiData' , u'nAxis' , u'nPosnClock' , u'nPosnDST' , u'nPosnWidth' , 
			u'nPosnLimit' , u'nVelClock' , u'nVelDST' , u'nVelWidth' , u'nVelLimit' , 
			), 143, (143, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 892 , (3, 0, None, None) , 0 , )),
	(( u'GetUserData' , u'bstrBody' , ), 144, (144, (), [ (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 896 , (3, 0, None, None) , 0 , )),
	(( u'PutUserData' , u'bstrBody' , ), 145, (145, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 900 , (3, 0, None, None) , 0 , )),
	(( u'GetAniSetup' , u'nAni' , u'nFilter' , ), 146, (146, (), [ (3, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 904 , (3, 0, None, None) , 0 , )),
	(( u'PutAniSetup' , u'nAni' , u'nFilter' , ), 147, (147, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 908 , (3, 0, None, None) , 0 , )),
	(( u'LoadAriesConfig' , u'bstrFile' , ), 148, (148, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 912 , (3, 0, None, None) , 0 , )),
	(( u'SaveAriesConfig' , u'bAries' , u'bstrFile' , ), 149, (149, (), [ (11, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 916 , (3, 0, None, None) , 0 , )),
	(( u'GetEPLData' , u'nNumberOfControlledNodes' , ), 150, (150, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 920 , (3, 0, None, None) , 0 , )),
	(( u'PutEPLData' , u'nTotalTraditionalAxes' , u'nNumberOfControlledNodes' , ), 151, (151, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 924 , (3, 0, None, None) , 0 , )),
	(( u'GetEPLNodeData' , u'nAxis' , u'nNodeID' , u'nMultiplexedCycleNumber' , u'nDriveMode' , 
			u'nTCPIPPortNumber' , u'nReserved1' , u'nReserved2' , ), 152, (152, (), [ (3, 1, None, None) , 
			(16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 928 , (3, 0, None, None) , 0 , )),
	(( u'PutEPLNodeData' , u'nAxis' , u'nNodeID' , u'nMultiplexedCycleNumber' , u'nDriveMode' , 
			u'nTCPIPPortNumber' , u'nReserved1' , u'nReserved2' , ), 153, (153, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 932 , (3, 0, None, None) , 0 , )),
	(( u'GetEPLDriveMotorData' , u'nAxis' , u'bIsAriesEPLSelected' , u'nSeriesSel' , u'nFrameSel' , 
			u'nStackSel' , u'nWindingSel' , u'nFeedbackSel' , u'nCustomPartNumberSel' , u'nBaseSeriesSel' , 
			u'strUserDefinedPartNumber' , u'nCustomWindingSel' , u'nCoolingSel' , u'nHeatSink' , u'bAdvancedSel' , 
			u'strFullPartNumber' , u'strHeatSink' , u'strCustomWindingNumber' , u'bIsCustomResolution' , ), 154, (154, (), [ 
			(3, 1, None, None) , (16395, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , 
			(16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16392, 2, None, None) , 
			(16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16395, 2, None, None) , (16392, 2, None, None) , 
			(16392, 2, None, None) , (16392, 2, None, None) , (16395, 2, None, None) , ], 1 , 1 , 4 , 0 , 936 , (3, 0, None, None) , 0 , )),
	(( u'PutEPLDriveMotorData' , u'nAxis' , u'bIsAriesEPLSelected' , u'nSeriesSel' , u'nFrameSel' , 
			u'nStackSel' , u'nWindingSel' , u'nFeedbackSel' , u'nCustomPartNumberSel' , u'nBaseSeriesSel' , 
			u'strUserDefinedPartNumber' , u'nCustomWindingSel' , u'nCoolingSel' , u'nHeatSink' , u'bAdvancedSel' , 
			u'strFullPartNumber' , u'strHeatSink' , u'strCustomWindingNumber' , u'bIsCustomResolution' , ), 155, (155, (), [ 
			(3, 1, None, None) , (11, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (11, 1, None, None) , (8, 1, None, None) , 
			(8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 940 , (3, 0, None, None) , 0 , )),
	(( u'GetEPLAdvancedDriveMotorData' , u'nAxis' , u'nMotorPackageSel' , u'strMotorPackage' , u'nPosFeedbackPackage' , 
			u'strMotorRatedSpeed' , u'strMotorPolePairs' , u'strMotorRotorInertia' , u'strMotorDamping' , u'strMotorThermalTimeConstant' , 
			u'strWindingThermalTimeConstant' , u'strWindingThermalResistance' , u'strMotorAmbientTemp' , u'strMaxMotorWindingTemp' , u'strKe' , 
			u'strContCurrent' , u'strContCurrentDerating' , u'strPeakCurrent' , u'strWindingResistance' , u'strMinInductance' , 
			u'strMaxInductance' , u'strFeedbackResolution' , u'nFeedbackTypeSel' , u'bInvertHallSignals' , ), 156, (156, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16392, 2, None, None) , (16387, 2, None, None) , (16392, 2, None, None) , 
			(16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , 
			(16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , 
			(16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , 
			(16392, 2, None, None) , (16387, 2, None, None) , (16395, 2, None, None) , ], 1 , 1 , 4 , 0 , 944 , (3, 0, None, None) , 0 , )),
	(( u'PutEPLAdvancedDriveMotorData' , u'nAxis' , u'nMotorPackageSel' , u'strMotorPackage' , u'nPosFeedbackPackage' , 
			u'strMotorRatedSpeed' , u'strMotorPolePairs' , u'strMotorRotorInertia' , u'strMotorDamping' , u'strMotorThermalTimeConstant' , 
			u'strWindingThermalTimeConstant' , u'strWindingThermalResistance' , u'strMotorAmbientTemp' , u'strMaxMotorWindingTemp' , u'strKe' , 
			u'strContCurrent' , u'strContCurrentDerating' , u'strPeakCurrent' , u'strWindingResistance' , u'strMinInductance' , 
			u'strMaxInductance' , u'strFeedbackResolution' , u'nFeedbackTypeSel' , u'bInvertHallSignals' , ), 157, (157, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , 
			(8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			(8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			(8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			(8, 1, None, None) , (3, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 948 , (3, 0, None, None) , 0 , )),
	(( u'GetFaultOutputThermalInputData' , u'nAxis' , u'bEnableFaultOnDriveDisable' , u'strOutputBrakeDelay' , u'bDisableMotorThermalSensor' , 
			u'nMotorThermalSensorTypeSel' , u'nMotorThermalSensorConstructionSel' , ), 158, (158, (), [ (3, 1, None, None) , (16395, 2, None, None) , 
			(16392, 2, None, None) , (16395, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 952 , (3, 0, None, None) , 0 , )),
	(( u'PutFaultOutputThermalInputData' , u'nAxis' , u'bEnableFaultOnDriveDisable' , u'strOutputBrakeDelay' , u'bDisableMotorThermalSensor' , 
			u'nMotorThermalSensorTypeSel' , u'nMotorThermalSensorConstructionSel' , ), 159, (159, (), [ (3, 1, None, None) , (11, 1, None, None) , 
			(8, 1, None, None) , (11, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 956 , (3, 0, None, None) , 0 , )),
	(( u'AutoTune' , u'fPGain' , u'fIGain' , u'fDGain' , u'nStatus' , 
			), 160, (160, (), [ (16388, 2, None, None) , (16388, 2, None, None) , (16388, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 960 , (3, 0, None, None) , 0 , )),
	(( u'GetEPLPeriod' , u'dEPLPeriod' , ), 161, (161, (), [ (16388, 2, None, None) , ], 1 , 1 , 4 , 0 , 964 , (3, 0, None, None) , 0 , )),
	(( u'PutEPLPeriod' , u'dEPLPeriod' , ), 162, (162, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 968 , (3, 0, None, None) , 0 , )),
	(( u'GetEPLDriveModeData' , u'nAxis' , u'nDriveControlMode' , u'bEnableCurrentFoldback' , u'nCommutationSel' , 
			u'nSwitchingFrequencySel' , u'bstrSwitchingFrequency' , u'bstrTorqueLimit' , u'bstrTorqueScaling' , u'bstrVelocityLimit' , 
			u'bstrVelocityScaling' , u'bstrProportionalGain' , u'bstrIntegralGain' , u'bstrIntegralLimit' , u'bstrBandwidth' , 
			u'bIAuto' , u'bstrPositionProportionalGain' , u'bstrPositionIntegralGain' , u'bstrPositionIntegralLimit' , u'bstrPositionVelocityGain' , 
			u'bstrPositionVelocityFeedforwardGain' , u'bstrVelocityProportionalGain' , u'bstrVelocityIntegralGain' , u'bstrVelocityIntegralLimit' , ), 163, (163, (), [ 
			(3, 1, None, None) , (16387, 2, None, None) , (16395, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , 
			(16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , 
			(16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , (16395, 2, None, None) , 
			(16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , 
			(16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 972 , (3, 0, None, None) , 0 , )),
	(( u'PutEPLDriveModeData' , u'nAxis' , u'nDriveControlMode' , u'bEnableCurrentFoldback' , u'nCommutationSel' , 
			u'nSwitchingFrequencySel' , u'bstrSwitchingFrequency' , u'bstrTorqueLimit' , u'bstrTorqueScaling' , u'bstrVelocityLimit' , 
			u'bstrVelocityScaling' , u'bstrProportionalGain' , u'bstrIntegralGain' , u'bstrIntegralLimit' , u'bstrBandwidth' , 
			u'bIAuto' , u'bstrPositionProportionalGain' , u'bstrPositionIntegralGain' , u'bstrPositionIntegralLimit' , u'bstrPositionVelocityGain' , 
			u'bstrPositionVelocityFeedforwardGain' , u'bstrVelocityProportionalGain' , u'bstrVelocityIntegralGain' , u'bstrVelocityIntegralLimit' , ), 164, (164, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (11, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			(8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , 
			(8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			(8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 976 , (3, 0, None, None) , 0 , )),
]

IControl_vtables_dispatch_ = 1
IControl_vtables_ = [
	(( u'bstrVersion' , u'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'nPort' , u'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'nPort' , u'pVal' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'nBPS' , u'pVal' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'nBPS' , u'pVal' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'bstrIP' , u'pVal' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'bstrIP' , u'pVal' , ), 4, (4, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'nBus' , u'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'nBus' , u'pVal' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'isOffline' , u'pVal' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'nMoveProfile' , u'pVal' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'nMoveProfile' , u'pVal' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'fMoveVEL' , u'pVal' , ), 8, (8, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'fMoveVEL' , u'pVal' , ), 8, (8, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'fMoveFVEL' , u'pVal' , ), 9, (9, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'fMoveFVEL' , u'pVal' , ), 9, (9, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'fMoveACC' , u'pVal' , ), 10, (10, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'fMoveACC' , u'pVal' , ), 10, (10, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'nMoveMode' , u'pVal' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'nMoveMode' , u'pVal' , ), 11, (11, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'bMoveAbsolute' , u'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'bMoveAbsolute' , u'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'nMoveCounter' , u'pVal' , ), 13, (13, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'nMoveCounter' , u'pVal' , ), 13, (13, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'nArcMode' , u'pVal' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'nArcMode' , u'pVal' , ), 14, (14, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'bArcAbsolute' , u'pVal' , ), 15, (15, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'bArcAbsolute' , u'pVal' , ), 15, (15, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'bArcCCW' , u'pVal' , ), 16, (16, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'bArcCCW' , u'pVal' , ), 16, (16, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'bOnConnectTest' , u'pVal' , ), 17, (17, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'bOnConnectTest' , u'pVal' , ), 17, (17, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'nCard' , u'pVal' , ), 18, (18, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'bstrUSBSerialNumber' , u'pVal' , ), 19, (19, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'bstrUSBSerialNumber' , u'pVal' , ), 19, (19, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'Disconnect' , ), 99, (99, (), [ ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'Connect' , u'nTransport' , u'nIndex' , ), 100, (100, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( u'SetFlag' , u'nBit' , u'bValue' , u'bFast' , ), 101, (101, (), [ 
			(3, 1, None, None) , (11, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'SetParmFloat' , u'nPparm' , u'fValue' , u'bFast' , ), 102, (102, (), [ 
			(3, 1, None, None) , (4, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( u'SetParmLong' , u'nPparm' , u'nValue' , u'bFast' , ), 103, (103, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'SetGlobal' , u'nCard' , u'nGlobal' , u'dValue' , u'bFast' , 
			), 104, (104, (), [ (3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( u'Move' , u'nMask' , u'targets' , ), 105, (105, (), [ (3, 1, None, None) , 
			(12, 1, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'Arc' , u'nMask' , u'targets' , ), 106, (106, (), [ (3, 1, None, None) , 
			(12, 1, None, None) , ], 1 , 1 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
	(( u'Stop' , u'bDecel' , ), 108, (108, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( u'SendRES' , u'nMask' , ), 109, (109, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
	(( u'TestConnect' , u'pVal' , ), 110, (110, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( u'SetWatchdog' , u'nInterval' , u'nRetries' , ), 111, (111, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 212 , (3, 0, None, None) , 0 , )),
	(( u'GetMoveCounter' , u'nCounter' , u'nIncrement' , ), 112, (112, (), [ (16387, 2, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( u'SetMoveCounter' , u'nCounter' , u'nIncrement' , ), 113, (113, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 220 , (3, 0, None, None) , 0 , )),
	(( u'SetACRMemory' , u'nType' , u'nAddress' , u'values' , ), 114, (114, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( u'SetACRMemoryMask' , u'nAddress' , u'nNAND' , u'nOR' , ), 115, (115, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 228 , (3, 0, None, None) , 0 , )),
	(( u'SetParmLongMask' , u'nPparm' , u'nNAND' , u'nOR' , ), 116, (116, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( u'SetFOV' , u'nMask' , u'fValue' , ), 117, (117, (), [ (3, 1, None, None) , 
			(4, 1, None, None) , ], 1 , 1 , 4 , 0 , 236 , (3, 0, None, None) , 0 , )),
	(( u'SetROV' , u'nMask' , u'fValue' , ), 118, (118, (), [ (3, 1, None, None) , 
			(4, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( u'InitPerformance' , ), 119, (119, (), [ ], 1 , 1 , 4 , 0 , 244 , (3, 0, None, None) , 0 , )),
	(( u'GetPerformance' , u'data' , ), 120, (120, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( u'MoveBatch' , u'nType' , u'moves' , ), 121, (121, (), [ (3, 1, None, None) , 
			(12, 1, None, None) , ], 1 , 1 , 4 , 0 , 252 , (3, 0, None, None) , 0 , )),
]

IStatus_vtables_dispatch_ = 1
IStatus_vtables_ = [
	(( u'bstrVersion' , u'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'nPort' , u'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'nPort' , u'pVal' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'nBPS' , u'pVal' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'nBPS' , u'pVal' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'bstrIP' , u'pVal' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'bstrIP' , u'pVal' , ), 4, (4, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'nBus' , u'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'nBus' , u'pVal' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'isOffline' , u'pVal' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'nStatusWaitRate' , u'pVal' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'nStatusWaitRate' , u'pVal' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'bOnConnectTest' , u'pVal' , ), 8, (8, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'bOnConnectTest' , u'pVal' , ), 8, (8, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'nCard' , u'pVal' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'bstrUSBSerialNumber' , u'pVal' , ), 10, (10, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'bstrUSBSerialNumber' , u'pVal' , ), 10, (10, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'Disconnect' , ), 99, (99, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Connect' , u'nTransport' , u'nIndex' , ), 100, (100, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'GetACRGroup' , u'bstrRequest' , u'Status' , ), 101, (101, (), [ (8, 1, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'GetACRCustom' , u'bstrRequest' , u'Status' , ), 102, (102, (), [ (8, 1, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'GetACRMemory' , u'nType' , u'nAddress' , u'nCount' , u'Status' , 
			), 103, (103, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'AddACRGroup' , u'bstrRequest' , u'nMsgid' , ), 104, (104, (), [ (8, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'AddACRCustom' , u'bstrRequest' , u'nMsgid' , ), 105, (105, (), [ (8, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'AddACRMemory' , u'nType' , u'nAddress' , u'nCount' , u'nMsgid' , 
			), 106, (106, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'GetStatus' , u'nMsgid' , u'Status' , ), 107, (107, (), [ (3, 1, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'DelStatus' , u'nMsgid' , ), 108, (108, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'GetLocalAddr' , u'nProg' , u'nType' , u'nSize' , u'nAddr' , 
			), 109, (109, (), [ (3, 1, None, None) , (3, 1, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'GetLocalArrayAddr' , u'nProg' , u'nType' , u'nArray' , u'nSize' , 
			u'nAddr' , ), 110, (110, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			(16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'IsFlagSet' , u'nFlagGrp' , u'nFlagNdx' , u'bFlagSet' , ), 111, (111, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'TestConnect' , u'pVal' , ), 112, (112, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'GetParmInfo' , u'nParameter' , u'nType' , u'nCode' , u'nIndex' , 
			u'bstrCatagory' , u'bstrDesc' , u'bFound' , ), 113, (113, (), [ (3, 1, None, None) , 
			(16387, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'SetWatchdog' , u'nInterval' , u'nRetries' , ), 114, (114, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'GetACRGroupRaw' , u'nType' , u'nCode' , u'nIndex' , u'Status' , 
			), 115, (115, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'AddACRGroupRaw' , u'nType' , u'nCode' , u'nIndex' , u'nMsgid' , 
			), 116, (116, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'GetParmType' , u'nParameter' , u'pVal' , ), 117, (117, (), [ (3, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'GetParmAddr' , u'nParameter' , u'nAddr' , ), 118, (118, (), [ (3, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
]

ITerminal_vtables_dispatch_ = 1
ITerminal_vtables_ = [
	(( u'bstrVersion' , u'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'nPort' , u'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'nPort' , u'pVal' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'nBPS' , u'pVal' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'nBPS' , u'pVal' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'bstrIP' , u'pVal' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'bstrIP' , u'pVal' , ), 4, (4, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'nBus' , u'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'nBus' , u'pVal' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'isOffline' , u'pVal' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'nDataWaitRate' , u'pVal' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'nDataWaitRate' , u'pVal' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'bOnConnectTest' , u'pVal' , ), 8, (8, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'bOnConnectTest' , u'pVal' , ), 8, (8, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'nCard' , u'pVal' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'bstrUSBSerialNumber' , u'pVal' , ), 10, (10, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'bstrUSBSerialNumber' , u'pVal' , ), 10, (10, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'Disconnect' , ), 99, (99, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Connect' , u'nTransport' , u'nIndex' , ), 100, (100, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'Read' , u'recv' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'Write' , u'send' , ), 102, (102, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'TestConnect' , u'pVal' , ), 103, (103, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'SetWatchdog' , u'nInterval' , u'nRetries' , ), 104, (104, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'TalkTo' , u'nMode' , u'nIndex' , u'nStatus' , ), 105, (105, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IUtility_vtables_dispatch_ = 1
IUtility_vtables_ = [
	(( u'bstrVersion' , u'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'nPort' , u'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'nPort' , u'pVal' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'nBPS' , u'pVal' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'nBPS' , u'pVal' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'bstrIP' , u'pVal' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'bstrIP' , u'pVal' , ), 4, (4, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'nBus' , u'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'nBus' , u'pVal' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'isOffline' , u'pVal' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'bOnConnectTest' , u'pVal' , ), 7, (7, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'bOnConnectTest' , u'pVal' , ), 7, (7, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'nCard' , u'pVal' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'bstrUSBSerialNumber' , u'pVal' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'bstrUSBSerialNumber' , u'pVal' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'Disconnect' , ), 99, (99, (), [ ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'Connect' , u'nTransport' , u'nIndex' , ), 100, (100, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'FindACR' , u'nTransport' , u'nDevices' , ), 101, (101, (), [ (3, 1, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'DownloadOS' , u'nDevice' , u'bstrFile' , ), 102, (102, (), [ (3, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'GetStatusDL' , u'nTotal' , u'nBytes' , u'nStatus' , ), 103, (103, (), [ 
			(16387, 2, None, None) , (16387, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'StopDownload' , ), 104, (104, (), [ ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'DownloadFile' , u'bstrPrg' , u'bstrFile' , ), 105, (105, (), [ (8, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'UploadFile' , u'bstrPrg' , u'bstrFile' , ), 106, (106, (), [ (8, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'TestConnect' , u'pVal' , ), 107, (107, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'DeviceIoControl' , u'dwloControlCode' , u'saBuffer' , u'rtn' , ), 108, (108, (), [ 
			(3, 1, None, None) , (16387, 3, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'DeviceIoControl2' , u'dwloControlCode' , u'saBuffer' , u'saBuffer2' , u'rtn' , 
			), 109, (109, (), [ (3, 1, None, None) , (16387, 3, None, None) , (16387, 3, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'SetWatchdog' , u'nInterval' , u'nRetries' , ), 110, (110, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'DownloadEPL' , u'nDevice' , u'bstrFile' , ), 111, (111, (), [ (3, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'DownloadAriesEPLOS' , u'nDevice' , u'bAllEPLDrives' , u'nAxis' , u'bstrFile' , 
			), 112, (112, (), [ (3, 1, None, None) , (11, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'GetStatusDLEx' , u'nTotal' , u'nBytes' , u'bstrExtendedErrorMessage' , u'nStatus' , 
			), 113, (113, (), [ (16387, 2, None, None) , (16387, 2, None, None) , (16392, 2, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{B1E87CFE-70A7-444D-9528-321F6928D4B4}' : Control,
	'{57DA70AA-3B42-4345-A3A4-C19756A5056A}' : IControl,
	'{D49EC970-1B96-4514-BE5A-BFC0E5AFFC4B}' : IUtility,
	'{454FE70D-5DC2-4128-A2C8-89B6D98F67C2}' : Status,
	'{E8393629-2EFE-428A-BF36-365A46940735}' : Terminal,
	'{548F6282-AEE7-4AFA-B1F6-8C85389DD697}' : _IStatusEvents,
	'{D71EADD4-66CD-44B2-A666-9A8A6D2FFD24}' : IStatus,
	'{1A2C9178-A91B-47B2-A883-63835A732D57}' : IConfig,
	'{36682CAC-F0A6-45B3-AD99-A1A6F8A5B05F}' : Config,
	'{A1C9E9E2-49BB-40A8-8A9B-301051D224F2}' : _ITerminalEvents,
	'{FB28DD27-1AC4-43B9-AFD7-8CA6003EEB7D}' : Utility,
	'{2EE309A6-546F-4FA4-B9AE-F76D91AA0133}' : ITerminal,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{D49EC970-1B96-4514-BE5A-BFC0E5AFFC4B}' : 'IUtility',
	'{57DA70AA-3B42-4345-A3A4-C19756A5056A}' : 'IControl',
	'{D71EADD4-66CD-44B2-A666-9A8A6D2FFD24}' : 'IStatus',
	'{1A2C9178-A91B-47B2-A883-63835A732D57}' : 'IConfig',
	'{2EE309A6-546F-4FA4-B9AE-F76D91AA0133}' : 'ITerminal',
}


NamesToIIDMap = {
	'IConfig' : '{1A2C9178-A91B-47B2-A883-63835A732D57}',
	'IControl' : '{57DA70AA-3B42-4345-A3A4-C19756A5056A}',
	'IUtility' : '{D49EC970-1B96-4514-BE5A-BFC0E5AFFC4B}',
	'ITerminal' : '{2EE309A6-546F-4FA4-B9AE-F76D91AA0133}',
	'_ITerminalEvents' : '{A1C9E9E2-49BB-40A8-8A9B-301051D224F2}',
	'IStatus' : '{D71EADD4-66CD-44B2-A666-9A8A6D2FFD24}',
	'_IStatusEvents' : '{548F6282-AEE7-4AFA-B1F6-8C85389DD697}',
}


