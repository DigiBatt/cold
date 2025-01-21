
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricPotentialModule import ElectricPotential



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity







class ElectrodePotential(ElectricPotential, ElectrochemicalQuantity):
    """
    Class representing the `ElectrodePotential` entity, which inherits from:
    - ElectricPotential, ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f509645f_eb27_470e_9112_7ab828ed40d3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrodePotential'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrodePotential(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f509645f_eb27_470e_9112_7ab828ed40d3',
    
    class_name='ElectrodePotential',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f509645f_eb27_470e_9112_7ab828ed40d3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrodePotential',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    