
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ActivationEnergyModule import ActivationEnergy







class NegativeElectrodeActivationEnergyOfReaction(ActivationEnergy):
    """
    Class representing the `NegativeElectrodeActivationEnergyOfReaction` entity, which inherits from:
    - ActivationEnergy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_fda9539d_5232_471c_8945_b9a8ec7247fe'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NegativeElectrodeActivationEnergyOfReaction'`
        - **Alias**: `class_name`
    
    - `bpxKey` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `bpxKey`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NegativeElectrodeActivationEnergyOfReaction(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_fda9539d_5232_471c_8945_b9a8ec7247fe',
    
    class_name='NegativeElectrodeActivationEnergyOfReaction',
    
    bpxKey="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_fda9539d_5232_471c_8945_b9a8ec7247fe',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NegativeElectrodeActivationEnergyOfReaction',
        alias="class_name"
    )
    
    bpxKey: Optional[str] = Field(
        None,
        alias="bpxKey"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    