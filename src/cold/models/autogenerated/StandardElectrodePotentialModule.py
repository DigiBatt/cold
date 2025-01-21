
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EquilibriumElectrodePotentialModule import EquilibriumElectrodePotential







class StandardElectrodePotential(EquilibriumElectrodePotential):
    """
    Class representing the `StandardElectrodePotential` entity, which inherits from:
    - EquilibriumElectrodePotential

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7fc10197_41d9_4c1e_a107_928f03eb2d36'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StandardElectrodePotential'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `dbpediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `dbpediaReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StandardElectrodePotential(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7fc10197_41d9_4c1e_a107_928f03eb2d36',
    
    class_name='StandardElectrodePotential',
    
    iupacReference="example_value",
    
    dbpediaReference="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7fc10197_41d9_4c1e_a107_928f03eb2d36',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StandardElectrodePotential',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    dbpediaReference: Optional[str] = Field(
        None,
        alias="dbpediaReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    