
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ActivationEnergyModule import ActivationEnergy







class ActivationEnergyOfGuestDiffusivityInPositiveElectrodeActiveMaterial(ActivationEnergy):
    """
    Class representing the `ActivationEnergyOfGuestDiffusivityInPositiveElectrodeActiveMaterial` entity, which inherits from:
    - ActivationEnergy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4d69edda_d2fa_40b0_9c1e_52e08debf578'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ActivationEnergyOfGuestDiffusivityInPositiveElectrodeActiveMaterial'`
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
    obj = ActivationEnergyOfGuestDiffusivityInPositiveElectrodeActiveMaterial(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4d69edda_d2fa_40b0_9c1e_52e08debf578',
    
    class_name='ActivationEnergyOfGuestDiffusivityInPositiveElectrodeActiveMaterial',
    
    cidemodKey="example_value",
    
    comment="example_value",
    
    elucidation="example_value",
    
    bpxKey="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4d69edda_d2fa_40b0_9c1e_52e08debf578',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ActivationEnergyOfGuestDiffusivityInPositiveElectrodeActiveMaterial',
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
    

    
    

    

    