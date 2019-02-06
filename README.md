# UniflocPY

## v1.0 02.2019

##### Authors:
**Rinat Khabibullin**
**Alexey Vodopyan**
**Artem Kiyan**
**Oleg Kobzar**
**Mikhail Poleshko**
**Artur Shabonas**

---
`*` – недоделанные функции

---
### Текущие возможности и реализованные функции:
---
#### uPVT
* ##### PVT_correlations – функции для расчета PVT-свойств
	* ###### Свойства нефти:
		 `unf_pb_Standing_MPaa` – расчет давления насыщения по корреляции Стендинга
		 `unf_pb_Valko_MPaa` – расчет давления насыщения по корреляции Валко-Маккейна
		`unf_pb_AlMarhoun_MPaa*` – расчет давления насыщения по корреляции Аль-Мархуна
		`unf_rs_Standing_m3m3` – расчет газосодержания по корреляции Стендинга
		`unf_rs_Velarde_m3m3` – расчет газосодержания по корреляции Веларде-Маккейна
		`unf_rsb_Mccain_m3m3` - расчет газосодержания при давлении насыщения с учетом потерь газа в сепараторе и резервуарах по корреляции Маккейна
		`unf_gamma_gas_Mccain` - расчет средневзвешенной относительной плотности газа по корреляции Маккейна
		`unf_fvf_Mccain_m3m3_below` - расчет объемного коэффициента нефти для давлений ниже давления насыщения по корреляции Маккейна
		`unf_fvf_VB_m3m3_above` - расчет объемного коэффициента нефти для давлений выше давления насыщения по соотношению Васкеса-Беггса (Стендинга)
		`unf_compressibility_oil_VB_1Mpa` - расчет сжимаемости нефти по корреляции Васкеса-Беггса
		`unf_fvf_Standing_m3m3_saturated` - расчет объемного коэффициента нефти при давлении насыщения по соотношению Стендинга
		`unf_density_oil_Mccain` - расчет плотности нефти по корреляции Маккейна
		`unf_density_oil_Standing` - расчет плотности нефти по корреляции Стендинга
		`unf_deadoilviscosity_Beggs_cP` - расчет вязкости дегазированной нефти по корреляции Беггса-Робинсона
		`unf_saturatedoilviscosity_Beggs_cP` - расчет вязкости нефти при давлениях ниже давления насыщения по корреляции Беггса-Робинсона
		`unf_undersaturatedoilviscosity_VB_cP` - расчет вязкости нефти при давлениях выше давления насыщения по корреляции Васкеса-Беггса
		`unf_undersaturatedoilviscosity_Petrovsky_cP` - расчет вязкости нефти при давлениях выше давления насыщения по корреляции Петровского-Фаршада
		`unf_oil_viscosity_Beggs_VB_cP` - расчет вязкости нефти при любом давлении(`unf_saturatedoilviscosity_Beggs_cP` + `unf_undersaturatedoilviscosity_VB_cP`)
		`unf_pb_Glaso_MPaa` - расчет давления насыщения по корреляции Глазо
		`unf_fvf_Glaso_m3m3_saturated` - расчет объемного коэффициента нефти при давлении насыщения по корреляции Глазо
		`unf_fvf_Glaso_m3m3_below` - расчет объемного коэффициента нефти при давлении ниже давления насыщения по корреляции Глазо
		`unf_McCain_specificgravity` - расчет относительной плотности газа в пластовых условиях по корреляции Маккейна
	* ###### Свойства газа:
		`unf_pseudocritical_temperature_K` - расчет псевдокритической температуры с учетом неуглеводородных газов по корреляции Пипера-Маккейна
		`unf_pseudocritical_pressure_MPa` - расчет псевдокритического давления с учетом неуглеводородных газов по корреляции Пипера-Маккейна
		`unf_zfactor_BrillBeggs` - расчет z-фактора по корреляции Беггса-Брилла
		`unf_zfactor_DAK` - расчет z-фактора по корреляции Дранчука-АбуКассема
		`unf_zfactor_DAK_ppr` - расчет z-фактора по корреляции Дранчука-АбуКассема (входные данные псевдокритические)
		`unf_compressibility_gas_Mattar_1MPa` - расчет сжимаемости газа по корреляции Маттара
		`unf_gasviscosity_Lee_cP` - расчет вязкости газа по корреляции Ли
		`unf_gas_fvf_m3m3` - расчет объемного коэффициента газа по соотношению
		`unf_gas_density_kgm3` - расчет плотности газа по соотношению
	* Свойства нефти с учетом газа*:
		`unf_weightedcompressibility_oil_Mccain_1MPa_greater` - расчет разных видов сжимаемости нефти, с учетом газа, не доделан
		`unf_compressibility_oil_Mccain_1MPa_greater` - расчет разных видов сжимаемости нефти, с учетом газа, не доделан
		`unf_compressibility_oil_Mccain_1MPa_lower` - расчет разных видов сжимаемости нефти, с учетом газа, не доделан
	* ###### Свойства воды:
		`unf_density_brine_Spivey_kgm3` - расчет плотности воды по корреляции Спиви-Маккейна
		`unf_compressibility_brine_Spivey_1MPa` - расчет сжимаемости воды по корреляции Спиви-Маккейна
		`unf_fvf_brine_Spivey_m3m3` - расчет объемного коэффициента воды по корреляции Спиви-Маккейна
		`unf_gwr_brine_Spivey_m3m3` - расчет газосодержания метана в воде по корреляции Спиви-Маккейна
		`unf_viscosity_brine_MaoDuan_cP` - расчет вязкости воды по корреляции Мао-Дуана
	* ###### class TestPVT - проверка расчета функций
* ##### PVT - классы для расчета свойств нефти, газа и воды
	* `class FluidBlackOil` - класс для расчета свойств нефти, газа и воды по модели Black Oil
		`calc*` - функция для расчета свойств нефти,газа и воды в зависимости давления и температуры в идеале хотели сделать по упрощенным линейным зависимостям
	* `class FluidStanding(FluidBlackOil)` - класс для расчета свойств нефти, газа и воды по набору корреляций Стендинга
		`calc` - функция для расчета свойств нефти, газа и воды в зависимости давления и температуры по набору корреляций Стендинга
	* `class FluidMcCain(FluidBlackOil)` - класс для расчета свойств нефти, газа и воды по набору корреляций Маккейна
		`calc` - функция для расчета свойств нефти, газа и воды в зависимости давления и температуры по набору корреляций Маккейна
---
#### uMultiphaseFlow
