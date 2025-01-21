
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalInterfaceModule import ElectrochemicalInterface







class ElectrodeElectrolyteInterface(ElectrochemicalInterface):
    """
    Class representing the `ElectrodeElectrolyteInterface` entity, which inherits from:
    - ElectrochemicalInterface

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9c73aff8_1c82_4116_a6be_78e21982b69d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrodeElectrolyteInterface'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrodeElectrolyteInterface(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9c73aff8_1c82_4116_a6be_78e21982b69d',
    
    class_name='ElectrodeElectrolyteInterface',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9c73aff8_1c82_4116_a6be_78e21982b69d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrodeElectrolyteInterface',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    