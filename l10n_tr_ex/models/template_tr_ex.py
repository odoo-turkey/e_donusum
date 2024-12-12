
from odoo import models, _
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = 'account.chart.template'

    @template('tr_ex')
    def _get_tr_ex_template_data(self):
        return {
            'name': _('Turkey Extended Accounting - 2KB Team)'),
            'parent': 'tr',
            'code_digits': '9',
            'property_account_receivable_id': 'tr120',
            'property_account_payable_id': 'tr320',
            'property_account_expense_categ_id': 'tr150',
            'property_account_income_categ_id': 'tr600',
        }

    @template('tr', 'res.company')
    def _get_tr_res_company(self):
        return {
            self.env.company.id: {
                'account_fiscal_country_id': 'base.tr',
                'bank_account_code_prefix': '102',
                'cash_account_code_prefix': '100',
                'transfer_account_code_prefix': '103',
                'account_default_pos_receivable_account_id': 'tr123',
                'income_currency_exchange_account_id': 'tr646',
                'expense_currency_exchange_account_id': 'tr656',
                'account_journal_suspense_account_id': 'tr102999',
                'account_journal_payment_debit_account_id': 'tr102997',
                'account_journal_payment_credit_account_id': 'tr102998',
                'account_sale_tax_id': 'tr_kdv_sale_20',
                'account_purchase_tax_id': 'tr_kdv_purchase_20'
            },
        }

    @template('tr_ex', 'account.account')
    def _get_tr_ex_account_account(self):
        tr_val = self._parse_csv('tr', 'account.account', module='l10n_tr')
        tr_ex_val = self._parse_csv('tr', 'account.account', module='l10n_tr_ex')
        return {**tr_val, **tr_ex_val}

    @template('tr_ex', 'account.tax.group')
    def _get_tr_ex_account_tax_group(self):
        return self._parse_csv('tr', 'account.tax.group', module='l10n_tr_ex')

    @template('tr_ex', 'account.tax')
    def _get_tr_ex_account_tax(self):
        return self._parse_csv('tr', 'account.tax', module='l10n_tr_ex')

    @template('tr_ex', 'account.fiscal.position')
    def _get_tr_ex_account_fiscal_position(self):
        return self._parse_csv('tr', 'account.fiscal.position', module='l10n_tr_ex')
