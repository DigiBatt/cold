
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricPotentialModule import ElectricPotential



from .ElectrochemicalThermodynamicQuantityModule import ElectrochemicalThermodynamicQuantity







class MembranePotential(ElectricPotential, ElectrochemicalThermodynamicQuantity):
    """
    Class representing the `MembranePotential` entity, which inherits from:
    - ElectricPotential, ElectrochemicalThermodynamicQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_601ff226_59b9_460b_90f5_2593450d96fa'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MembranePotential'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MembranePotential(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_601ff226_59b9_460b_90f5_2593450d96fa',
    
    class_name='MembranePotential',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_601ff226_59b9_460b_90f5_2593450d96fa',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MembranePotential',
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
    

    
    

    

    