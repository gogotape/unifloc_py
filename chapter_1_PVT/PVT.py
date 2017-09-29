# -*- coding: utf-8 -*-
"""
Created on Mon Sept 04 2017

@author: rnt

UniflocPy

класс для расчета PVT свойств углеводородных флюидов и воды

"""


class ComponentGeneral:
    """
    Абстрактный класс для описания компонентоы углеводородных флюидов
    """
    def __init__(self):
        self.gamma = 1          # specific gravity of component, dimensionless
        self.rho_kgm3 = 800       # density with dimension
        self.mu_cp = 1          # dynamic viscosity
        """ термобарические условия """
        self._p_bar = 1
        self._t_c = 15

    def calc(self, p_atm, t_c):
        """ recalculate all parameters according to some pressure and termperature"""
        return 1


class GasGeneral(ComponentGeneral):
    """
    Класс для описания свойств углеводородных газов
    """
    def __init__(self):
        super().__init__()
        self._z = 0.9               # сверхсжимаемость

    @property
    def z(self):
        return  self._z


class OilGeneral(ComponentGeneral):
    """
    Класс для описания свойств нефти по модели нелетучей нефти
    """
    def __init__(self):
        super().__init__()              # часть базовых свойств наследуется
        self._gas = GasGeneral()        # create gas component
        self.rsb_m3m3 = 100

        self.pb_calibr_bar = 100        # калибровочное значение давления насыщения
        self.tb_calibr_c = 50           # температуры для калибровки по давлению насыщения
        self.bob_calibr_m3m3 = 1.2      # калибровочное значение объемного коэффициента
        self.muob_calibr_cp = 1         # калибровочное значение вязкости при давлении насыщения

        """ расчетные свойства """
        self._rs_m3m3 = 1
        self._bo_m3m3 = 1
        self._mu_cp = 1

    @property
    def gas(self):
        return self._gas

    @property
    def rs_m3m3(self):
        """ газосодержание """
        return self._rs_m3m3

    def _calc_rs_m3m3(self, p_bar, t_c):
        """ тут должна быть реализация расчета газосодержания
        """
        if p_bar < self.pb_calibr_bar:
            return self.rsb_m3m3 / self.pb_calibr_bar * p_bar
        else:
            return self.rsb_m3m3


    def _calc_rho_kgm3(self, p_bar, t_c):
        """ тут должна быть реализация расчета газосодержания
        """
        if p_bar < self.pb_calibr_bar:
            return - p_bar + 800
        else:
            return 700







    def calc(self, p_atm, t_c):
        """ реализация расчета свойств нефти """
        self._rs_m3m3 = self._calc_rs_m3m3(p_atm, t_c)
        self.rho_kgm3 = self._calc_rho_kgm3(p_atm, t_c)

if __name__ == "__main__":
    print("Вы запустили модуль напрямую, а не импортировали его.")
    input ("\n\nНажмите Enter, чтобы выйти.")