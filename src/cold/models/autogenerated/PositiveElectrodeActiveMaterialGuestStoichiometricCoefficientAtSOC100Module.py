
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StoichiometricCoefficientAtSOC100Module import StoichiometricCoefficientAtSOC100







class PositiveElectrodeActiveMaterialGuestStoichiometricCoefficientAtSOC100(StoichiometricCoefficientAtSOC100):
    """
    Class representing the `PositiveElectrodeActiveMaterialGuestStoichiometricCoefficientAtSOC100` entity, which inherits from:
    - StoichiometricCoefficientAtSOC100

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_99041897_5c08_40ed_9118_3e77e9b0e191'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PositiveElectrodeActiveMaterialGuestStoichiometricCoefficientAtSOC100'`
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
    obj = PositiveElectrodeActiveMaterialGuestStoichiometricCoefficientAtSOC100(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_99041897_5c08_40ed_9118_3e77e9b0e191',
    
    class_name='PositiveElectrodeActiveMaterialGuestStoichiometricCoefficientAtSOC100',
    
    cidemodKey="example_value",
    
    bpxKey="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_99041897_5c08_40ed_9118_3e77e9b0e191',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PositiveElectrodeActiveMaterialGuestStoichiometricCoefficientAtSOC100',
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
    

    
    

    

    