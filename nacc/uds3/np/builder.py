###############################################################################
# Copyright 2015-2016 University of Florida. All rights reserved.
# This file is part of UF CTS-IT's NACCulator project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

from nacc.uds3 import blanks
import forms as np_forms
from nacc.uds3 import packet as np_packet


def build_uds3_np_form(record):
    packet = np_packet.Packet()
    np = np_forms.FormNP()
    np.NPFORMMO = record['npformmo']
    np.NPFORMDY = record['npformdy']
    np.NPFORMYR = record['npformyr']
    np.NPID = record['npid']
    np.NPSEX = record['npsex']
    np.NPDAGE = record['npdage']
    np.NPDODMO = record['npdodmo']
    np.NPDODDY = record['npdoddy']
    np.NPDODYR = record['npdodyr']
    np.NPPMIH = record['nppmih']
    np.NPFIX = record['npfix']
    np.NPFIXX = record['npfixx']
    np.NPWBRWT = record['npwbrwt']
    np.NPWBRF = record['npwbrf']
    np.NPGRCCA = record['npgrcca']
    np.NPGRLA = record['npgrla']
    np.NPGRHA = record['npgrha']
    np.NPGRSNH = record['npgrsnh']
    np.NPGRLCH = record['npgrlch']
    np.NPAVAS = record['npavas']
    np.NPTAN = record['nptan']
    np.NPTANX = record['nptanx']
    np.NPABAN = record['npaban']
    np.NPABANX = record['npabanx']
    np.NPASAN = record['npasan']
    np.NPASANX = record['npasanx']
    np.NPTDPAN = record['nptdpan']
    np.NPTDPANX = record['nptdpanx']
    np.NPHISMB = record['nphismb']
    np.NPHISG = record['nphisg']
    np.NPHISSS = record['nphisss']
    np.NPHIST = record['nphist']
    np.NPHISO = record['nphiso']
    np.NPHISOX = record['nphisox']
    np.NPTHAL = record['npthal']
    np.NPBRAAK = record['npbraak']
    np.NPNEUR = record['npneur']
    np.NPADNC = record['npadnc']
    np.NPDIFF = record['npdiff']
    np.NPAMY = record['npamy']
    np.NPINF = record['npinf']
    np.NPINF1A = record['npinf1a']
    np.NPINF1B = record['npinf1b']
    np.NPINF1D = record['npinf1d']
    np.NPINF1F = record['npinf1f']
    np.NPINF2A = record['npinf2a']
    np.NPINF2B = record['npinf2b']
    np.NPINF2D = record['npinf2d']
    np.NPINF2F = record['npinf2f']
    np.NPINF3A = record['npinf3a']
    np.NPINF3B = record['npinf3b']
    np.NPINF3D = record['npinf3d']
    np.NPINF3F = record['npinf3f']
    np.NPINF4A = record['npinf4a']
    np.NPINF4B = record['npinf4b']
    np.NPINF4D = record['npinf4d']
    np.NPINF4F = record['npinf4f']
    np.NPHEMO = record['nphemo']
    np.NPHEMO1 = record['nphemo1']
    np.NPHEMO2 = record['nphemo2']
    np.NPHEMO3 = record['nphemo3']
    np.NPOLD = record['npold']
    np.NPOLD1 = record['npold1']
    np.NPOLD2 = record['npold2']
    np.NPOLD3 = record['npold3']
    np.NPOLD4 = record['npold4']
    np.NPOLDD = record['npoldd']
    np.NPOLDD1 = record['npoldd1']
    np.NPOLDD2 = record['npoldd2']
    np.NPOLDD3 = record['npoldd3']
    np.NPOLDD4 = record['npoldd4']
    np.NPARTER = record['nparter']
    np.NPWMR = record['npwmr']
    np.NPPATH = record['nppath']
    np.NPNEC = record['npnec']
    np.NPPATH2 = record['nppath2']
    np.NPPATH3 = record['nppath3']
    np.NPPATH4 = record['nppath4']
    np.NPPATH5 = record['nppath5']
    np.NPPATH6 = record['nppath6']
    np.NPPATH7 = record['nppath7']
    np.NPPATH8 = record['nppath8']
    np.NPPATH9 = record['nppath9']
    np.NPPATH10 = record['nppath10']
    np.NPPATH11 = record['nppath11']
    np.NPPATHO = record['nppatho']
    np.NPPATHOX = record['nppathox']
    np.NPLBOD = record['nplbod']
    np.NPNLOSS = record['npnloss']
    np.NPHIPSCL = record['nphipscl']
    np.NPTDPA = record['nptdpa']
    np.NPTDPB = record['nptdpb']
    np.NPTDPC = record['nptdpc']
    np.NPTDPD = record['nptdpd']
    np.NPTDPE = record['nptdpe']
    np.NPFTDTAU = record['npftdtau']
    np.NPPICK = record['nppick']
    np.NPFTDT2 = record['npftdt2']
    np.NPCORT = record['npcort']
    np.NPPROG = record['npprog']
    np.NPFTDT5 = record['npftdt5']
    np.NPFTDT6 = record['npftdt6']
    np.NPFTDT7 = record['npftdt7']
    np.NPFTDT8 = record['npftdt8']
    np.NPFTDT9 = record['npftdt9']
    np.NPFTDT10 = record['npftdt10']
    np.NPFTDTDP = record['npftdtdp']
    np.NPALSMND = record['npalsmnd']
    np.NPOFTD = record['npoftd']
    np.NPOFTD1 = record['npoftd1']
    np.NPOFTD2 = record['npoftd2']
    np.NPOFTD3 = record['npoftd3']
    np.NPOFTD4 = record['npoftd4']
    np.NPOFTD5 = record['npoftd5']
    np.NPPDXA = record['nppdxa']
    np.NPPDXB = record['nppdxb']
    np.NPPDXC = record['nppdxc']
    np.NPPDXD = record['nppdxd']
    np.NPPDXE = record['nppdxe']
    np.NPPDXF = record['nppdxf']
    np.NPPDXG = record['nppdxg']
    np.NPPDXH = record['nppdxh']
    np.NPPDXI = record['nppdxi']
    np.NPPDXJ = record['nppdxj']
    np.NPPDXK = record['nppdxk']
    np.NPPDXL = record['nppdxl']
    np.NPPDXM = record['nppdxm']
    np.NPPDXN = record['nppdxn']
    np.NPPDXO = record['nppdxo']
    np.NPPDXP = record['nppdxp']
    np.NPPDXQ = record['nppdxq']
    np.NPPDXR = record['nppdxr']
    np.NPPDXRX = record['nppdxrx']
    np.NPPDXS = record['nppdxs']
    np.NPPDXSX = record['nppdxsx']
    np.NPPDXT = record['nppdxt']
    np.NPPDXTX = record['nppdxtx']
    np.NPBNKA = record['npbnka']
    np.NPBNKB = record['npbnkb']
    np.NPBNKC = record['npbnkc']
    np.NPBNKD = record['npbnkd']
    np.NPBNKE = record['npbnke']
    np.NPBNKF = record['npbnkf']
    np.NPBNKG = record['npbnkg']
    np.NPFAUT = record['npfaut']
    np.NPFAUT1 = record['npfaut1']
    np.NPFAUT2 = record['npfaut2']
    np.NPFAUT3 = record['npfaut3']
    np.NPFAUT4 = record['npfaut4']
    packet.append(np)

    update_header(record, packet)
    return packet

def update_header(record, packet):
    for header in packet:
        #header.PACKET = "I"
        #header.FORMID = header.form_name
        header.FORMVER = 10
        header.ADCID = record['adcid']
        header.PTID = record['ptid']
        '''
        header.VISITMO = record['visitmo']
        header.VISITDAY = record['visitday']
        header.VISITYR = record['visityr']
        header.VISITNUM = record['visitnum']
        header.INITIALS = record['initials']
        '''