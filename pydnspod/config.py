#!/usr/bin/python
#coding=utf-8

USER_AGENT = "pydnspod/0.01(lxl1217@gmail.com)"
DEFAULT_FORMAT = "json"
DEFAULT_LANG = "en"
LOGIN_REMEMBER = "yes"

PARAMS = {
    "Info.Version": {"required": [], "optional": []},
    "User.Detail": {"required": [], "optional": []},
    "User.Modify": {"required": [("real_name", "nick", "telephone", "im")], "optional": []},
    "Userpasswd.Modify": {"required": ["old_password", "new_password"], "optional": []},
    "Usermail.Modify": {"required": ["old_email", "new_email", "password"], "optional": []},
    "Telephoneverify.Code": {"required": ["telephone"], "optional": []},
    "User.Log": {"required": [], "optional": []},
    "Domain.Create": {"required": ["domain"], "optional": ["group_id", "is_mark"]},
    "Domain.List": {"required": [], "optional": ["type", "offset", "length", "group_id"]},
    "Domain.Remove": {"required": [("domain_id", "domain")], "optional": []},
    "Domain.Status": {"required": [("domain_id", "domain"), "status"], "optional": []},
    "Domain.Info": {"required": [("domain_id", "domain")], "optional": []},
    "Domain.Log": {"required": [("domain_id", "domain")], "optional": []},
    "Domain.Searchenginepush": {"required": [("domain_id", "domain"), "status"], "optional": []},
    "Domainshare.Create": {"required": [("domain_id", "domain"), "email"], "optional": ["mode", "sub_domain"]},
    "Domainshare.Modify": {"required": [("domain_id", "domain"), "email"], "optional": ["mode", "old_sub_domain", "new_sub_domain" ]},
    "Domainshare.Remove": {"required": [("domain_id", "domain"), "email"], "optional": []},
    "Domain.Transfer": {"required": [("domain_id", "domain"), "email"], "optional": []},
    "Domain.Lock": {"required": ["domain_id", "days"], "optional": []},
    "Domain.Lockstatus": {"required": [("domain_id", "domain")], "optional": []},
    "Domain.Unlock": {"required": [("domain_id", "domain"), "lock_code"], "optional": []},
    "Domainalias.List": {"required": [("domain_id", "domain")], "optional": []},
    "Domainalias.Create": {"required": ["domain_id", "domain"], "optional": []},
    "Domainalias.Remove": {"required": [("domain_id", "domain"), "alias_id"], "optional": []},
    "Domaingroup.List": {"required": [], "optional": []},
    "Domaingroup.Create": {"required": ["group_name"], "optional": []},
    "Domaingroup.Modify": {"required": ["group_id", "group_name"], "optional": []},
    "Domaingroup.Remove": {"required": ["group_id"], "optional": []},
    "Domain.Changegroup": {"required": [("domain_id", "domain"), "group_id"], "optional": []},
    "Domain.Ismark": {"required": [("domain_id", "domain"), "is_mark"], "optional": []},
    "Domain.Remark": {"required": [("domain_id", "domain"), "remark"], "optional": []},
    "Domain.Purview": {"required": [("domain_id", "domain")], "optional": []},
    "Domain.Acquire": {"required": [("domain")], "optional": []},
    "Domain.Acquiresend": {"required": ["domain", "email"], "optional": []},
    "Domain.Acquirevalidate": {"required": ["domain", "code"], "optional": []},
    "Record.Type": {"required": ["domain_grade"], "optional": []},
    "Record.Line": {"required": [("domain_id", "domain"), "domain_grade"], "optional": []},
    "Record.Create": {"required": ["domain_id", "record_type", "record_line", "value"], "optional": ["sub_domain", "mx", "ttl"]},
    "Record.List": {"required": ["domain_id"], "optional": ["length", "offset", "sub_domain"]},
    "Record.Modify": {"required": ["domain_id", "record_id", "record_type", "record_line", "value"], "optional": ["sub_domain", "mx", "ttl"]},
    "Record.Remove": {"required": ["domain_id", "record_id"], "optional": []},
    "Record.Ddns": {"required": ["domain_id", "record_id", "record_line", "sub_domain"], "optional": ["value"]},
    "Record.Remark": {"required": ["domain_id", "record_id", "remark"], "optional": []},
    "Record.Info": {"required": ["domain_id", "record_id"], "optional": []},
    "Record.Status": {"required": ["domain_id", "record_id"], "optional": ["status"]},
    "Monitor.Listsubdomain": {"required": [("domain_id", "domain")], "optional": []},
    "Monitor.Listsubvalue": {"required": [("domain_id", "domain"), "subdomain"], "optional": []},
    "Monitor.List": {"required": [], "optional": []},
    "Monitor.Create": {"required": ["domain_id", "record_id", "port", "monitor_interval", "host", "monitor_type", "monitor_path", "points", "bak_ip"], "optional": ["email_notice", "sms_notice", "less_notice", "keep_ttl", "callback_url", "callback_key"]},
    "Monitor.Modify": {"required": ["monitor_id", "port", "monitor_interval", "monitor_type", "monitor_path", "points", "bak_ip"], "optional": ["sms_notice", "email_notice", "less_notice", "callback_url", "callback_key"]},
    "Monitor.Remove": {"required": ["monitor_id"], "optional": []},
    "Monitor.Info": {"required": ["monitor_id"], "optional": []},
    "Monitor.Setstatus": {"required": ["monitor_id", "status"], "optional": []},
    "Monitor.Gethistory": {"required": ["monitor_id"], "optional": ["hours"]},
    "Monitor.Userdesc": {"required": [], "optional": []},
    "Monitor.Getdowns": {"required": [], "optional": ["offset", "length"]},
}
