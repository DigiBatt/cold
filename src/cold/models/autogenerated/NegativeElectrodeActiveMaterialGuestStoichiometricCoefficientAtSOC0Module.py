
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StoichiometricCoefficientAtSOC0Module import StoichiometricCoefficientAtSOC0







class NegativeElectrodeActiveMaterialGuestStoichiometricCoefficientAtSOC0(StoichiometricCoefficientAtSOC0):
    """
    Class representing the `NegativeElectrodeActiveMaterialGuestStoichiometricCoefficientAtSOC0` entity, which inherits from:
    - StoichiometricCoefficientAtSOC0

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_21da0fe9_9fb6_4840_a12f_fbcc1ba84fb3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NegativeElectrodeActiveMaterialGuestStoichiometricCoefficientAtSOC0'`
        - **Alias**: `class_name`
    
    - `cidemodKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `cidemodKey`
    
    - `bpxKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `bpxKey`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NegativeElectrodeActiveMaterialGuestStoichiometricCoefficientAtSOC0(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_21da0fe9_9fb6_4840_a12f_fbcc1ba84fb3',
    
    class_name='NegativeElectrodeActiveMaterialGuestStoichiometricCoefficientAtSOC0',
    
    cidemodKey="example_value",
    
    bpxKey="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_21da0fe9_9fb6_4840_a12f_fbcc1ba84fb3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NegativeElectrodeActiveMaterialGuestStoichiometricCoefficientAtSOC0',
        alias="class_name"
    )
    
    cidemodKey: Optional[str] = Field(
        None,
        alias="cidemodKey"
    )
    
    bpxKey: Optional[str] = Field(
        None,
        alias="bpxKey"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    