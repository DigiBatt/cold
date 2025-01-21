
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ActivationEnergyModule import ActivationEnergy







class ActivationEnergyOfChargeCarrierDiffusivityInElectrolyte(ActivationEnergy):
    """
    Class representing the `ActivationEnergyOfChargeCarrierDiffusivityInElectrolyte` entity, which inherits from:
    - ActivationEnergy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_56de36fe_e8e1_486c_8d29_061ac8d28c13'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ActivationEnergyOfChargeCarrierDiffusivityInElectrolyte'`
        - **Alias**: `class_name`
    
    - `cidemodKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `cidemodKey`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `bpxKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `bpxKey`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ActivationEnergyOfChargeCarrierDiffusivityInElectrolyte(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_56de36fe_e8e1_486c_8d29_061ac8d28c13',
    
    class_name='ActivationEnergyOfChargeCarrierDiffusivityInElectrolyte',
    
    cidemodKey="example_value",
    
    comment="example_value",
    
    elucidation="example_value",
    
    bpxKey="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_56de36fe_e8e1_486c_8d29_061ac8d28c13',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ActivationEnergyOfChargeCarrierDiffusivityInElectrolyte',
        alias="class_name"
    )
    
    cidemodKey: Optional[str] = Field(
        None,
        alias="cidemodKey"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    bpxKey: Optional[str] = Field(
        None,
        alias="bpxKey"
    )
    

    
    

    

    