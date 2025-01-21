
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaximumConcentrationModule import MaximumConcentration







class NegativeElectrodeActiveMaterialMaximumGuestConcentration(MaximumConcentration):
    """
    Class representing the `NegativeElectrodeActiveMaterialMaximumGuestConcentration` entity, which inherits from:
    - MaximumConcentration

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e808a26a_5812_49e9_894c_b793c7fe0c38'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NegativeElectrodeActiveMaterialMaximumGuestConcentration'`
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
    obj = NegativeElectrodeActiveMaterialMaximumGuestConcentration(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e808a26a_5812_49e9_894c_b793c7fe0c38',
    
    class_name='NegativeElectrodeActiveMaterialMaximumGuestConcentration',
    
    cidemodKey="example_value",
    
    comment="example_value",
    
    elucidation="example_value",
    
    bpxKey="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e808a26a_5812_49e9_894c_b793c7fe0c38',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NegativeElectrodeActiveMaterialMaximumGuestConcentration',
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
    

    
    

    

    