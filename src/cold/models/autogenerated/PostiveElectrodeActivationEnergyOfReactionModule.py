
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ActivationEnergyModule import ActivationEnergy







class PostiveElectrodeActivationEnergyOfReaction(ActivationEnergy):
    """
    Class representing the `PostiveElectrodeActivationEnergyOfReaction` entity, which inherits from:
    - ActivationEnergy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_56b9cd1f_5397_4385_9292_30d93d9e7a05'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PostiveElectrodeActivationEnergyOfReaction'`
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
    obj = PostiveElectrodeActivationEnergyOfReaction(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_56b9cd1f_5397_4385_9292_30d93d9e7a05',
    
    class_name='PostiveElectrodeActivationEnergyOfReaction',
    
    bpxKey="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_56b9cd1f_5397_4385_9292_30d93d9e7a05',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PostiveElectrodeActivationEnergyOfReaction',
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
    

    
    

    

    